from collections import Counter
from datetime import datetime


def generate_report(source_name, findings, risk_score, risk_level):
    severity_counts = Counter(
        finding.get("severity", "Unknown")
        for finding in findings
    )

    category_counts = Counter(
        finding.get("category", "Unknown")
        for finding in findings
    )

    return {
        "source": source_name,
        "scan_time": datetime.now().isoformat(timespec="seconds"),
        "risk_score": risk_score,
        "risk_level": risk_level,
        "total_findings": len(findings),
        "severity_counts": dict(severity_counts),
        "category_counts": dict(category_counts),
        "findings": findings
    }
