RULES = [
    {
        "id": "SEC001",
        "category": "Hardcoded Secrets",
        "severity": "High",
        "description": "Potential hardcoded password, API key, token, or secret detected.",
        "recommendation": "Move secrets to environment variables or a secure secret manager."
    },
    {
        "id": "SEC002",
        "category": "SQL Injection",
        "severity": "High",
        "description": "Potential SQL injection caused by unsafe string construction.",
        "recommendation": "Use parameterized queries or prepared statements."
    },
    {
        "id": "SEC003",
        "category": "Command Injection",
        "severity": "Critical",
        "description": "Potential command injection through unsafe command execution.",
        "recommendation": "Avoid shell execution with untrusted input and use safe argument-based APIs."
    },
    {
        "id": "SEC004",
        "category": "Dangerous Function Usage",
        "severity": "High",
        "description": "Use of a potentially dangerous Python function detected.",
        "recommendation": "Avoid unsafe execution functions and validate all inputs."
    },
    {
        "id": "SEC005",
        "category": "Weak Cryptography",
        "severity": "Medium",
        "description": "Use of a weak or outdated cryptographic algorithm detected.",
        "recommendation": "Use modern cryptographic algorithms and secure configurations."
    },
    {
        "id": "SEC006",
        "category": "Insecure File Handling",
        "severity": "Medium",
        "description": "Potentially unsafe file handling pattern detected.",
        "recommendation": "Validate file paths and restrict access to trusted locations."
    },
    {
        "id": "SEC007",
        "category": "Input Validation",
        "severity": "Medium",
        "description": "Potentially unvalidated external input detected.",
        "recommendation": "Validate, sanitize, and constrain untrusted input before use."
    },
    {
        "id": "SEC008",
        "category": "Suspicious Security Pattern",
        "severity": "Low",
        "description": "A suspicious security-related coding pattern was detected.",
        "recommendation": "Review the flagged code and apply appropriate security controls."
    }
]
