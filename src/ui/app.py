from __future__ import annotations

import requests
import streamlit as st

from config.settings import get_settings
from src.ui.components import (
    footer,
    header,
    metrics,
    report,
    uploader,
)
from src.ui.theme import load_theme

settings = get_settings()

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

load_theme()

header()

# ----------------------------------------------------
# Incident Input
# ----------------------------------------------------

uploaded, text, scan = uploader()

content = ""

if uploaded is not None:
    content = uploaded.read().decode("utf-8", errors="ignore")

elif text.strip():
    content = text.strip()

# ----------------------------------------------------
# Scan
# ----------------------------------------------------

if scan:

    if not content:
        st.warning("Please upload an incident file or paste incident text.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    status.info("🔍 Parser Agent scanning incident...")
    progress.progress(20)

    status.info("🧠 Investigation Agent assessing risk...")
    progress.progress(45)

    status.info("⚖️ Decision Agent determining response...")
    progress.progress(70)

    status.info("📝 Report Agent generating executive report...")
    progress.progress(90)

    try:

        response = requests.post(
            settings.api_url,
            json={
                "source": "streamlit",
                "content": content,
            },
            timeout=180,
        )

        response.raise_for_status()
        st.session_state["result"] = response.json()
        progress.progress(100)

        status.success("✅ Investigation completed successfully.")

    except Exception as ex:
        progress.empty()
        status.empty()
        st.error(f"Guardian API Error\n\n{ex}")
        st.stop()

# ----------------------------------------------------
# Results
# ----------------------------------------------------

if "result" in st.session_state:
    result = st.session_state["result"]
    metrics(result)
    report(result["report"])

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

footer()