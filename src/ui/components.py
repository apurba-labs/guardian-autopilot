import streamlit as st


def header():

    st.title("🛡 Guardian Autopilot")

    st.caption(
        "AI-Powered Multi-Agent Incident Response Platform"
    )

    st.divider()


def uploader():

    st.subheader("Incident Source")

    uploaded = st.file_uploader(
        "Upload Incident File",
        type=["txt"],
    )

    st.markdown("### OR")

    text = st.text_area(
        "Paste Incident",
        height=220,
    )

    scan = st.button(
        "🛡 Scan Incident",
        use_container_width=True,
    )

    return uploaded, text, scan


def metrics(result):

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Risk",
        result["risk"],
    )

    c2.metric(
        "Decision",
        result["decision"],
    )

    c3.metric(
        "State",
        result["state"],
    )


def report(report):

    st.subheader("Executive Report")

    st.code(
        report["content"],
        language="text",
    )

    st.download_button(
        "Download Report",
        report["content"],
        file_name="guardian_report.txt",
    )


def footer():

    st.divider()

    st.caption(
        "Powered by Alibaba Cloud Qwen • Guardian Autopilot v1.0"
    )