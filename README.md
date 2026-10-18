# SecureScan — Secure Code Vulnerability Scanner & Risk Analyzer

SecureScan is a Python-based Static Application Security Testing (SAST) tool for detecting selected security vulnerabilities and suspicious coding patterns in Python source code.

It combines Python AST analysis, pattern-based detection, custom security rules, severity classification, risk analysis, security recommendations, and an interactive Streamlit dashboard.

**SecureScan analyzes source code statically and does not execute the analyzed Python code.**

---

## 🔗 Project Links

- **GitHub Repository:** https://github.com/mdsakibhasan-cs/SecureScan
- **Live Demo:** Add your deployed Streamlit URL here after deployment

---

## 🎯 Project Overview

SecureScan was developed as a practical cybersecurity and software-engineering project focused on Static Application Security Testing.

### Analysis Pipeline

Source Code  
→ AST Parsing  
→ Pattern Analysis  
→ Security Rule Engine  
→ Vulnerability Detection  
→ Severity Classification  
→ Risk Analysis  
→ Security Recommendations  
→ Security Report  
→ Interactive Dashboard

The project demonstrates practical application of:

- Cybersecurity
- Secure Software Engineering
- Static Application Security Testing
- Python AST analysis
- Vulnerability detection
- Security rule engineering
- Risk prioritization
- Automated testing
- Interactive security dashboards

---

## ✨ Key Features

- Python source-code security scanning
- AST-based source-code analysis
- Regular-expression pattern analysis
- Custom security rule engine
- Hardcoded secret detection
- SQL injection pattern detection
- Command injection detection
- Dangerous function detection
- Weak cryptography detection
- Insecure file-handling detection
- Severity classification
- Custom risk-score calculation
- Risk-level classification
- Security recommendations
- Detailed vulnerability findings
- JSON security-report generation
- Interactive Streamlit dashboard
- Vulnerable and safer reference samples
- Automated testing with Pytest
- Static analysis without executing analyzed source code

---

## 🛡️ Security Rules

SecureScan currently defines eight security rules.

### SEC001 — Hardcoded Secrets

Detects potential hardcoded passwords, API keys, tokens, and similar secret-related assignments.

**Severity:** High

**Recommendation:** Move secrets to environment variables or a secure secret manager.

---

### SEC002 — SQL Injection

Detects selected potentially unsafe SQL execution patterns.

**Severity:** High

**Recommendation:** Use parameterized queries or prepared statements.

---

### SEC003 — Command Injection

Detects selected potentially dangerous command-execution patterns, including unsafe use of system-level command functions.

**Severity:** Critical

**Recommendation:** Avoid shell execution with untrusted input and use safe argument-based APIs.

---

### SEC004 — Dangerous Function Usage

Detects potentially dangerous Python functions such as `eval()` and `exec()`.

**Severity:** High

**Recommendation:** Avoid unsafe dynamic execution functions and validate inputs.

---

### SEC005 — Weak Cryptography

Detects selected weak or outdated cryptographic algorithms, including:

- MD5
- SHA-1
- DES
- RC4

**Severity:** Medium

**Recommendation:** Use modern cryptographic algorithms and secure configurations.

---

### SEC006 — Insecure File Handling

Detects selected potentially unsafe file-handling patterns.

**Severity:** Medium

**Recommendation:** Validate file paths and restrict file access to trusted locations.

---

### SEC007 — Input Validation

Defines a rule for potentially unvalidated external input.

**Severity:** Medium

**Recommendation:** Validate, sanitize, and constrain untrusted input before use.

**Implementation status:** The rule is currently defined, but an active detector for this category has not yet been implemented.

---

### SEC008 — Suspicious Security Pattern

Defines a rule for suspicious security-related coding patterns.

**Severity:** Low

**Recommendation:** Review the flagged code and apply appropriate security controls.

**Implementation status:** The rule is currently defined, but an active detector for this category has not yet been implemented.

---

## 🚨 Severity Levels

| Severity | Weight | Priority |
|---|---:|---|
| Critical | 10 | Immediate attention |
| High | 7 | High priority |
| Medium | 4 | Moderate priority |
| Low | 1 | Lower priority |

---

## 📊 Risk Analysis

SecureScan calculates a custom risk score based on the severity of detected findings.

### Severity Weights

- Critical = 10
- High = 7
- Medium = 4
- Low = 1

### Formula

Risk Score = (Total Finding Severity Weight / Maximum Possible Severity Weight) × 100

The maximum possible severity weight for each finding is 10.

The final score is limited to 100 and rounded to two decimal places.

### Risk Levels

| Risk Score | Risk Level |
|---:|---|
| 75–100 | Critical |
| 50–74.99 | High |
| 25–49.99 | Medium |
| 0–24.99 | Low |

> The risk score is a custom prioritization metric created for this project. It is not a CVSS score and should not be interpreted as a complete measurement of application security.

---

## 🏗️ Project Architecture

    SecureScan/
    ├── scanner/
    │   ├── __init__.py
    │   ├── parser.py
    │   ├── detector.py
    │   ├── rules.py
    │   ├── severity.py
    │   ├── risk.py
    │   ├── reporter.py
    │   └── scanner.py
    │
    ├── tests/
    │   └── test_scanner.py
    │
    ├── samples/
    │   ├── vulnerable_app.py
    │   └── safer_app.py
    │
    ├── reports/
    ├── screenshots/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    └── LICENSE

---

## 🧩 Core Components

### `scanner/parser.py`

Parses Python source code using the built-in Python `ast` module and identifies syntax errors.

### `scanner/detector.py`

Contains the main vulnerability-detection logic.

It combines:

- AST analysis
- Regular expressions
- Security rules
- Assignment analysis
- Function-call analysis
- Pattern analysis

Detected vulnerabilities are returned as structured findings.

### `scanner/rules.py`

Contains centralized security-rule definitions.

Each rule includes:

- Rule ID
- Category
- Severity
- Description
- Recommendation

### `scanner/severity.py`

Contains severity weights used by the risk-analysis system.

### `scanner/risk.py`

Calculates:

- Risk score
- Risk level

### `scanner/reporter.py`

Generates structured security reports containing:

- Source filename
- Scan timestamp
- Risk score
- Risk level
- Total findings
- Severity counts
- Category counts
- Detailed findings

### `scanner/scanner.py`

Provides the main scanning interface.

The `scan_source()` function:

1. Receives Python source code.
2. Detects vulnerabilities.
3. Calculates the risk score.
4. Determines the risk level.
5. Generates the final report.

---

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| Static Analysis | Python AST |
| Pattern Detection | Regular Expressions |
| Security Analysis | Custom SAST Rules |
| Dashboard | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly |
| Testing | Pytest |
| Version Control | Git / GitHub |
| Environment | Python Virtual Environment |

---

## 📋 Requirements

Before running SecureScan, install:

- Python 3.10+
- pip
- Git
- Python virtual-environment support

---

## 🚀 Installation

### 1. Clone the Repository

    git clone https://github.com/mdsakibhasan-cs/SecureScan.git
    cd SecureScan

### 2. Create a Virtual Environment

#### Windows

    python -m venv .venv
    .venv\Scripts\Activate.ps1

#### Linux / macOS

    python3 -m venv .venv
    source .venv/bin/activate

### 3. Install Dependencies

    pip install -r requirements.txt

---

## ▶️ Run the Dashboard

Start the application with:

    python -m streamlit run app.py

Streamlit will display the local application URL in the terminal.

Open the displayed URL in a web browser.

---

## 📖 Usage

1. Open the SecureScan dashboard.
2. Upload a Python `.py` file or paste Python source code.
3. Click **Scan Code**.
4. SecureScan parses the source code.
5. The scanner performs static security analysis.
6. Detected findings are classified by severity.
7. A risk score is calculated.
8. A risk level is assigned.
9. Security recommendations are displayed.
10. Detailed findings can be reviewed.
11. A JSON security report can be downloaded.

**The uploaded or pasted source code is analyzed statically and is not executed by SecureScan.**

---

## 🔍 Reference Vulnerable Sample

The repository includes a reference vulnerable application demonstrating multiple insecure coding patterns.

    import os
    import hashlib
    import sqlite3

    password = "admin123"
    api_key = "ABC123SECRET"

    user_input = input("Enter command: ")
    os.system(user_input)

    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    connection = sqlite3.connect("users.db")
    connection.execute(query)

    hashlib.md5(password.encode())

    with open(user_input, "r") as file:
        data = file.read()

    eval(user_input)

This sample is intended for demonstrating the scanner's detection capabilities.

---

## 📈 Verified Vulnerable Sample Results

The current reference vulnerable sample produces:

| Metric | Result |
|---|---:|
| Total Findings | 7 |
| Risk Score | 65.71 |
| Risk Level | High |

### Detected Findings

| Rule | Category | Findings | Severity |
|---|---|---:|---|
| SEC001 | Hardcoded Secrets | 2 | High |
| SEC002 | SQL Injection | 1 | High |
| SEC003 | Command Injection | 1 | Critical |
| SEC004 | Dangerous Function Usage | 1 | High |
| SEC005 | Weak Cryptography | 1 | Medium |
| SEC006 | Insecure File Handling | 1 | Medium |

**Total: 7 findings**

---

## 🔐 Reference Safer Sample

The repository also includes a safer reference implementation demonstrating several secure-coding practices.

    import os
    import sqlite3
    from pathlib import Path

    password = os.environ.get("APP_PASSWORD")

    user_input = input("Enter username: ").strip()

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE name = ?",
        (user_input,)
    )

    safe_directory = Path("data").resolve()
    requested_file = (safe_directory / "example.txt").resolve()

    if requested_file.is_relative_to(safe_directory):
        with requested_file.open("r", encoding="utf-8") as file:
            data = file.read()

    print(data)

The sample demonstrates:

- Environment-based secret handling
- Parameterized SQL queries
- Path validation
- Avoidance of unsafe dynamic execution
- Safer file handling

---

## 📉 Verified Safer Sample Results

The current safer reference sample produces:

| Metric | Result |
|---|---:|
| Total Findings | 0 |
| Risk Score | 0.0 |
| Risk Level | Low |

> A zero-finding result does not guarantee that the source code is secure. It only means that the currently implemented detection rules did not identify a finding in the tested sample.

---

## 🧪 Automated Testing

SecureScan includes automated tests covering:

- Vulnerable sample detection
- Safer sample detection
- Empty source code
- Syntax-error source code

Run the test suite with:

    pytest

### Current Verified Test Result

    4 passed

The vulnerable-sample test verifies:

- 7 findings
- Risk level: High
- Risk score: 65.71

The safer-sample test verifies:

- 0 findings
- Risk level: Low
- Risk score: 0.0

---

## 🔬 Static Analysis Method

SecureScan does not execute the analyzed application.

The scanner follows this process:

    Python Source Code
            |
            v
       AST Parsing
            |
            v
     Pattern Analysis
            |
            v
    Security Rule Engine
            |
            v
    Vulnerability Findings
            |
            v
    Severity Classification
            |
            v
        Risk Score
            |
            v
     Recommendations
            |
            v
     Security Report

This architecture allows SecureScan to inspect source code while avoiding execution of potentially unsafe input.

---

## 📊 Dashboard

The Streamlit dashboard provides an interactive security-analysis interface.

It includes:

- Python source-code input
- Python file upload
- Scan Code action
- Risk score
- Risk level
- Finding statistics
- Severity distribution
- Category distribution
- Detailed findings
- Security recommendations
- JSON report download

---

## 📄 Security Reports

SecureScan generates structured reports containing:

- Source
- Scan time
- Risk score
- Risk level
- Total findings
- Severity counts
- Category counts
- Detailed findings

Individual findings contain information such as:

- Rule ID
- Category
- Severity
- Description
- Recommendation
- Line number
- Source-code line

---

## 🔎 Detection Approach

### Hardcoded Secrets

The scanner checks selected secret-related assignment names, including:

- password
- passwd
- api_key
- secret
- token
- access_key

Supported environment-based patterns using `os.environ` and `os.getenv` are excluded from the hardcoded-secret detection logic.

### Command Injection

The scanner checks selected command-execution functions, including:

- `os.system()`
- `os.popen()`

### Dangerous Functions

The scanner detects:

- `eval()`
- `exec()`

### SQL Injection

The scanner checks selected `.execute()` call patterns.

Calls with multiple arguments are treated as parameterized-query patterns by the current implementation.

This is a pattern-based implementation and is not a complete SQL data-flow or taint-analysis engine.

### Weak Cryptography

The scanner checks selected weak algorithms, including:

- MD5
- SHA-1
- DES
- RC4

### Insecure File Handling

The scanner checks selected `open()` patterns and recognizes a limited safe-path pattern.

This is not a complete filesystem-security or path-traversal analysis engine.

---

## ⚠️ Limitations

SecureScan is an educational, research, and portfolio-oriented SAST project.

It is not intended to replace professional security-analysis platforms.

Current limitations include:

- Detection is focused on selected Python security patterns.
- Static pattern matching can produce false positives.
- Static analysis can miss vulnerabilities.
- Complex application-level data flows are not fully modeled.
- Cross-file analysis is not implemented.
- Full interprocedural analysis is not implemented.
- Full taint analysis is not implemented.
- SQL injection detection is pattern-based.
- Command-injection detection is limited to selected functions.
- File-handling detection is pattern-based.
- SEC007 currently has no active detector.
- SEC008 currently has no active detector.
- The risk score is a custom prioritization metric.
- The scanner currently focuses on Python source code.
- A zero-finding result does not guarantee that the source code is secure.
- Findings should be manually reviewed before production use.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Expanded vulnerability-rule coverage
- Advanced data-flow analysis
- Taint analysis
- Cross-file analysis
- Interprocedural analysis
- Improved SQL injection analysis
- Improved command-injection detection
- Expanded input-validation detection
- CWE mapping
- CVSS-inspired prioritization
- SARIF report generation
- HTML security reports
- PDF security reports
- CI/CD integration
- GitHub Actions security scanning
- Automated pull-request security scanning
- Additional programming-language support
- More comprehensive test coverage
- Improved false-positive reduction
- Configurable security rules
- User-defined security rules

---

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Python application development
- Python AST analysis
- Regular-expression pattern matching
- Static security analysis
- Vulnerability detection
- Security-rule engineering
- Risk scoring
- Secure coding concepts
- Streamlit application development
- Data visualization
- Automated testing
- Software architecture
- Git and GitHub workflow

---

## 🎯 Project Purpose

SecureScan was developed to gain practical experience in:

- Static Application Security Testing
- Secure software development
- Source-code analysis
- Vulnerability detection
- Security rule engineering
- Risk prioritization
- Automated security testing
- Security reporting
- Interactive security applications

---

## ✅ Project Validation

The current implementation has been validated using reference source-code samples and automated tests.

### Vulnerable Sample

- Findings: 7
- Risk Score: 65.71
- Risk Level: High

### Safer Sample

- Findings: 0
- Risk Score: 0.0
- Risk Level: Low

### Automated Tests

- Tests passed: 4

These results are specific to the included reference samples and test cases and should not be interpreted as complete vulnerability-detection coverage.

---

## 🛡️ Security Disclaimer

SecureScan is provided for educational, research, and portfolio purposes.

The scanner does not guarantee that analyzed software is secure.

A zero-finding result does not mean that an application contains no vulnerabilities.

Detected findings should be reviewed and validated by qualified developers or security professionals.

For production applications, SecureScan should be used as one component of a broader secure software-development and security-testing process.

---

## 📜 License

This project is intended to be released under the MIT License.

See the `LICENSE` file for the complete license text.

---

## 👨‍💻 Author

**MD Sakib Hasan**

Computer Science and Technology  
Nantong University

### Areas of Interest

- Cybersecurity
- Secure Software Engineering
- Software Development
- Artificial Intelligence
- Machine Learning
- Static Code Analysis

---

## 📌 Project Status

**Completed Portfolio Project**

The current implementation includes:

- Core security scanner
- AST-based analysis
- Security rules
- Vulnerability detection
- Severity classification
- Risk analysis
- Security recommendations
- Streamlit dashboard
- JSON reporting
- Vulnerable reference sample
- Safer reference sample
- Automated testing

**Current verified test status: 4 passed**