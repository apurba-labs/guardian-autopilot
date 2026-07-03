import streamlit as st


def load_theme() -> None:
    st.set_page_config(
        page_title="Guardian Autopilot",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        .risk-critical{
            color:#ef4444;
            font-weight:bold;
            font-size:28px;
        }

        .risk-high{
            color:#f97316;
            font-weight:bold;
        }

        .risk-medium{
            color:#facc15;
            font-weight:bold;
        }

        .risk-low{
            color:#22c55e;
            font-weight:bold;
        }

        footer{
            visibility:hidden;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )