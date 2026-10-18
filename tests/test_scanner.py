from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scanner.scanner import scan_source


def test_vulnerable_sample():
    source = Path("samples/vulnerable_app.py").read_text(encoding="utf-8")

    result = scan_source(source, "vulnerable_app.py")

    assert result["total_findings"] == 7
    assert result["risk_level"] == "High"
    assert result["risk_score"] == 65.71


def test_safer_sample():
    source = Path("samples/safer_app.py").read_text(encoding="utf-8")

    result = scan_source(source, "safer_app.py")

    assert result["total_findings"] == 0
    assert result["risk_level"] == "Low"
    assert result["risk_score"] == 0.0


def test_empty_source():
    result = scan_source("", "empty.py")

    assert result["total_findings"] == 0
    assert result["risk_score"] == 0.0
    assert result["risk_level"] == "Low"


def test_syntax_error_source():
    source = "def broken(:"

    result = scan_source(source, "broken.py")

    assert result["total_findings"] == 0
    assert result["risk_score"] == 0.0
    assert result["risk_level"] == "Low"
