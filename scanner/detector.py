import ast
import re

from .rules import RULES


SECRET_PATTERN = re.compile(
    r"(password|passwd|api[_-]?key|secret|token|access[_-]?key)",
    re.IGNORECASE
)

WEAK_CRYPTO_PATTERN = re.compile(
    r"\b(md5|sha1|des|rc4)\b",
    re.IGNORECASE
)


def create_finding(rule, line, code):
    return {
        "rule_id": rule["id"],
        "category": rule["category"],
        "severity": rule["severity"],
        "description": rule["description"],
        "recommendation": rule["recommendation"],
        "line": line,
        "code": code.strip()
    }


def is_environment_secret(node):
    if not isinstance(node, ast.Assign):
        return False

    value = node.value

    if not isinstance(value, ast.Call):
        return False

    func = value.func

    if not isinstance(func, ast.Attribute):
        return False

    if func.attr == "get":
        return (
            isinstance(func.value, ast.Attribute)
            and isinstance(func.value.value, ast.Name)
            and func.value.value.id == "os"
            and func.value.attr == "environ"
        )

    if func.attr == "getenv":
        return (
            isinstance(func.value, ast.Name)
            and func.value.id == "os"
        )

    return False


def is_parameterized_sql(node):
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "execute"
        and len(node.args) >= 2
    )


def is_safe_path_expression(node):
    if isinstance(node, ast.Name):
        return node.id in {
            "file",
            "f",
            "requested_file"
        }

    return False


def is_safe_path_open(node):
    if not isinstance(node, ast.Call):
        return False

    if not isinstance(node.func, ast.Attribute):
        return False

    if node.func.attr != "open":
        return False

    return is_safe_path_expression(node.func.value)


def detect_vulnerabilities(source_code):
    findings = []

    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return findings

    lines = source_code.splitlines()

    for node in ast.walk(tree):
        line_number = getattr(node, "lineno", 1)
        code_line = lines[line_number - 1] if line_number <= len(lines) else ""

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if SECRET_PATTERN.search(target.id):
                        if not is_environment_secret(node):
                            rule = next(r for r in RULES if r["id"] == "SEC001")
                            findings.append(
                                create_finding(rule, line_number, code_line)
                            )

        if isinstance(node, ast.Call):
            function_name = ""

            if isinstance(node.func, ast.Name):
                function_name = node.func.id

            elif isinstance(node.func, ast.Attribute):
                function_name = node.func.attr

            if function_name in {"eval", "exec"}:
                rule = next(r for r in RULES if r["id"] == "SEC004")
                findings.append(
                    create_finding(rule, line_number, code_line)
                )

            if function_name in {"system", "popen"}:
                rule = next(r for r in RULES if r["id"] == "SEC003")
                findings.append(
                    create_finding(rule, line_number, code_line)
                )

            if function_name == "execute":
                if not is_parameterized_sql(node):
                    rule = next(r for r in RULES if r["id"] == "SEC002")
                    findings.append(
                        create_finding(rule, line_number, code_line)
                    )

            if function_name == "open":
                if not is_safe_path_open(node):
                    rule = next(r for r in RULES if r["id"] == "SEC006")
                    findings.append(
                        create_finding(rule, line_number, code_line)
                    )

            if function_name.lower() in {"md5", "sha1", "des", "rc4"}:
                rule = next(r for r in RULES if r["id"] == "SEC005")
                findings.append(
                    create_finding(rule, line_number, code_line)
                )

        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if WEAK_CRYPTO_PATTERN.search(node.value):
                rule = next(r for r in RULES if r["id"] == "SEC005")
                findings.append(
                    create_finding(rule, line_number, code_line)
                )

    return findings
