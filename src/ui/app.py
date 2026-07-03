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

load_theme()

header()

uploaded, text, scan = uploader()

content = ""

if uploaded:
    content = uploaded.read().decode()

elif text.strip():
    content = text

if scan:

    if not content:

        st.error(
            "Please upload or paste an incident."
        )

        st.stop()

    with st.spinner("Guardian Autopilot is analyzing..."):

        response = requests.post(
            settings.api_url,
            json={
                "source": "streamlit",
                "content": content,
            },
            timeout=180,
        )

        st.session_state["result"] = response.json()

if "result" in st.session_state:

    result = st.session_state["result"]

    metrics(result)

    report(result["report"])

footer()