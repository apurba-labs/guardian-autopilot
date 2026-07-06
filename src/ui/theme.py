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

/* ---------- Layout ---------- */

.block-container{
    max-width:1200px;
    padding-top:1.5rem;
    padding-bottom:2rem;
}

.main{
    padding-top:0rem;
}

/* ---------- Hide Streamlit ---------- */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* ---------- Buttons ---------- */

.stButton > button{

    width:100%;

    height:48px;

    border-radius:10px;

    font-weight:600;

    border:none;

    transition:.25s;
}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:0 6px 18px rgba(0,0,0,.15);
}

/* ---------- Download ---------- */

.stDownloadButton > button{

    width:100%;

    height:46px;

    border-radius:10px;

    font-weight:600;
}

/* ---------- File uploader ---------- */

[data-testid="stFileUploader"]{

    border:2px dashed #d1d5db;

    border-radius:12px;

    padding:1rem;
}

/* ---------- Metrics ---------- */

div[data-testid="stMetric"]{

    border:1px solid #e5e7eb;

    border-radius:12px;

    background:#ffffff;

    padding:18px;

    box-shadow:0 2px 8px rgba(0,0,0,.05);
}

/* ---------- Text Area ---------- */

textarea{

    border-radius:10px !important;
}

/* ---------- Code Block ---------- */

.stCodeBlock{

    border-radius:12px;
}

/* ---------- Alert ---------- */

[data-testid="stAlert"]{

    border-radius:10px;
}

/* ---------- Divider ---------- */

hr{

    margin-top:1.5rem;

    margin-bottom:1.5rem;
}

/* ---------- Caption ---------- */

.caption{

    color:#6b7280;
}

/* ---------- Mobile ---------- */

@media (max-width:768px){

.block-container{

    padding-left:1rem;

    padding-right:1rem;

}

}

</style>
""",
        unsafe_allow_html=True,
    )