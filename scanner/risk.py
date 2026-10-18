def calculate_risk_score(findings):
    if not findings:
        return 0.0

    weights = {
        "Critical": 10,
        "High": 7,
        "Medium": 4,
        "Low": 1
    }

    total_weight = sum(
        weights.get(finding.get("severity"), 0)
        for finding in findings
    )

    max_possible_weight = len(findings) * 10

    if max_possible_weight == 0:
        return 0.0

    score = (total_weight / max_possible_weight) * 100

    return round(min(score, 100.0), 2)


def get_risk_level(score):
    if score >= 75:
        return "Critical"
    if score >= 50:
        return "High"
    if score >= 25:
        return "Medium"
    return "Low"
