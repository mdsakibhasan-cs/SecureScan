import ast


def parse_code(source_code):
    try:
        return ast.parse(source_code)
    except SyntaxError as error:
        return {
            "error": str(error),
            "line": error.lineno,
            "offset": error.offset
        }
