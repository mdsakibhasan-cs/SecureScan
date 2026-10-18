from pathlib import Path
import streamlit as st
from scanner.scanner import scan_source


st.set_page_config(
    page_title="SecureScan",
    page_icon="Secure",
    layout="wide"
)


st.title("SecureScan")
st.subheader("Secure Code Vulnerability Scanner & Risk Analyzer")

st.write(
    "Static analysis tool for detecting potential security "
    "vulnerabilities in Python source code."
)

st.divider()


uploaded_file = st.file_uploader(
    "Upload a Python source file",
    type=["py"]
)

source_code = st.text_area(
    "Or paste Python code here",
    height=300,
    placeholder="Paste your Python source code here..."
)


if uploaded_file is not None:
    source_code = uploaded_file.read().decode("utf-8")
    source_name = uploaded_file.name
else:
    source_name = "pasted_code.py"


if st.button("Scan Code", type="primary"):

    if not source_code.strip():
        st.warning("Please upload a Python file or paste Python code.")
    else:
        report = scan_source(
            source_code,
            source_name
        )

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Risk Score",
            f"{report['risk_score']:.2f}"
        )

        col2.metric(
            "Risk Level",
            report["risk_level"]
        )

        col3.metric(
            "Total Findings",
            report["total_findings"]
        )

        col4.metric(
            "Source",
            report["source"]
        )

        st.divider()

        st.subheader("Severity Summary")

        severity_counts = report.get(
            "severity_counts",
            {}
        )

        if severity_counts:
            severity_columns = st.columns(
                max(len(severity_counts), 1)
            )

            for column, (severity, count) in zip(
                severity_columns,
                severity_counts.items()
            ):
                column.metric(
                    severity,
                    count
                )
        else:
            st.success(
                "No security findings detected."
            )

        if severity_counts:
            st.subheader("Severity Distribution")

            severity_chart_data = {
                "Severity": list(severity_counts.keys()),
                "Count": list(severity_counts.values())
            }

            st.bar_chart(
                severity_chart_data,
                x="Severity",
                y="Count"
            )

        category_counts = report.get(
            "category_counts",
            {}
        )

        if category_counts:
            st.subheader("Category Distribution")

            category_chart_data = {
                "Category": list(category_counts.keys()),
                "Count": list(category_counts.values())
            }

            st.bar_chart(
                category_chart_data,
                x="Category",
                y="Count"
            )

        st.divider()

        st.subheader("Download Security Report")

        import json

        report_json = json.dumps(
            report,
            indent=2,
            ensure_ascii=False
        )

        st.download_button(
            label="Download JSON Report",
            data=report_json,
            file_name=f"{Path(report["source"]).stem}_security_report.json",
            mime="application/json"
        )

        st.divider()

        st.subheader("Security Findings")

        if report["findings"]:

            for index, finding in enumerate(
                report["findings"],
                start=1
            ):
                with st.expander(
                    f"{index}. {finding['rule_id']} - "
                    f"{finding['category']} "
                    f"({finding['severity']})"
                ):

                    st.write(
                        f"Line: {finding['line']}"
                    )

                    st.code(
                        finding["code"],
                        language="python"
                    )

                    st.write(
                        f"Description: "
                        f"{finding['description']}"
                    )

                    st.info(
                        f"Recommendation: "
                        f"{finding['recommendation']}"
                    )

        else:
            st.success(
                "No potential vulnerabilities were detected."
            )

        st.divider()

        st.caption(
            f"Scan completed: {report['scan_time']}"
        )
