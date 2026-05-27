import streamlit as st

st.set_page_config(
    page_title="CitizenAssist AI",
    page_icon="⚖️",
    layout="wide"
)

st.title("🇮🇳 CitizenAssist AI")
st.subheader(
    "Your AI Guide for Government Services & Legal Support"
)

st.write("""
Ask questions about:
- Government Schemes
- Legal Guidance
- Complaint Help
""")

user_input = st.text_input(
    "Ask your question:"
)

if user_input:
    st.success(
        f"You asked: {user_input}"
    )