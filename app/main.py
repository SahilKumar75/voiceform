import json
import os

import streamlit as st

st.set_page_config(page_title="VoiceForm", page_icon=None, layout="centered")

with open(os.path.join(os.path.dirname(__file__), "schema.json")) as f:
    SCHEMA = json.load(f)

FIELD_LABELS = {
    "applicant_name": "Name / नाम",
    "date_of_birth": "Date of Birth / जन्म तिथि",
    "state_of_domicile": "State / राज्य",
    "community_category": "Category / श्रेणी",
    "annual_family_income": "Annual Income / वार्षिक आय",
    "bank_account_number": "Bank Account / बैंक खाता",
    "bank_ifsc_code": "IFSC Code",
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600&family=Inter:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', 'Noto Sans Devanagari', sans-serif;
        background-color: #FAF7F2;
        color: #1C1C1C;
    }
    .block-container {
        max-width: 480px;
        padding-top: 3rem;
    }
    h1 {
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        color: #1B2A4A;
    }
    .subtitle {
        text-align: center;
        color: #1C1C1C;
        margin-bottom: 2rem;
        font-size: 1rem;
    }
    .mic-button {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background-color: #FF9933;
        margin: 0 auto 2.5rem auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        color: #FAF7F2;
        box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }
    .field-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.9rem 1rem;
        margin-bottom: 0.6rem;
        border-radius: 10px;
        background-color: #FFFFFF;
        border: 1px solid #E7E1D6;
    }
    .field-label {
        font-size: 0.95rem;
        color: #1B2A4A;
        font-weight: 600;
    }
    .field-value {
        font-size: 0.95rem;
        color: #8A8478;
    }
    .status-note {
        text-align: center;
        color: #8A8478;
        font-size: 0.85rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>VoiceForm</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Fill your scholarship form by speaking / बोलकर फॉर्म भरें</div>",
    unsafe_allow_html=True,
)

st.markdown("<div class='mic-button'>&#127908;</div>", unsafe_allow_html=True)

for field in SCHEMA["required"]:
    label = FIELD_LABELS.get(field, field)
    st.markdown(
        f"<div class='field-row'><span class='field-label'>{label}</span>"
        f"<span class='field-value'>not filled yet</span></div>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<div class='status-note'>Placeholder UI only, voice input and ASR are not wired up yet.</div>",
    unsafe_allow_html=True,
)
