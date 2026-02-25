import streamlit as st

st.set_page_config(
    page_title="Trustworthy AI — Overview Demo",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ Trustworthy AI — Overview Demo")
st.caption("A simple Streamlit demo for politicians and management: what Trustworthy AI is and why it matters.")

st.success("Start here: open **Interactive mini-demo (story mode)** in the left menu.")

st.markdown(
    """
### Trustworthy AI in one line
**Trustworthy AI** means AI that is **Reliable, Safe, Fair, Transparent, and Accountable**.

This demo helps you **explain those five ideas clearly** using one simple scenario and interactive visuals.
"""
)

st.divider()
st.markdown(
    """
### Suggested 5–7 minute presentation flow
1) Open **Interactive mini-demo (story mode)**  
2) Click through: **Reliable → Safe → Fair → Transparent → Accountable**  
3) End with the **Roadmap** page
"""
)
