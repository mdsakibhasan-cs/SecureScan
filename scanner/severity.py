SEVERITY_WEIGHTS = {
    "Critical": 10,
    "High": 7,
    "Medium": 4,
    "Low": 1
}


def get_severity_weight(severity):
    return SEVERITY_WEIGHTS.get(severity, 0)
