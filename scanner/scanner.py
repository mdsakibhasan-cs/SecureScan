from .detector import detect_vulnerabilities
from .risk import calculate_risk_score, get_risk_level
from .reporter import generate_report


def scan_source(source_code, source_name="uploaded_code.py"):
    findings = detect_vulnerabilities(source_code)

    risk_score = calculate_risk_score(findings)
    risk_level = get_risk_level(risk_score)

    report = generate_report(
        source_name=source_name,
        findings=findings,
        risk_score=risk_score,
        risk_level=risk_level
    )

    return report
