import streamlit as st

st.set_page_config(
    page_title="Trustworthy AI — Overview Demo",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ Trustworthy AI — Overview Demo")
st.caption("A politician- and management-friendly Streamlit demo: what it is, why it matters, and what to do about it.")

col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown(
        """
### One-sentence definition
**Trustworthy AI** means AI systems that are **reliable, safe, fair, transparent, and accountable** — so we can use them
without unexpected harm, discrimination, or loss of public trust.

### How to use this demo
Use the pages on the left:
1. **What is Trustworthy AI?**
2. **Why should we care?**
3. **Interactive mini-demo**
4. **Failure stories**
5. **Roadmap**
        """
    )

with col2:
    st.info(
        """
**Audience:** politicians, directors, public-sector leaders, and decision makers.

**Purpose:** explain *why Trustworthy AI is a policy & governance issue*, not a purely technical detail.
        """
    )
    st.success("Tip: start with **Interactive mini-demo** for the fastest impact.")

st.divider()
st.markdown(
    """
### Core message
AI can be helpful, but it can also fail — quietly, unfairly, or out of context.
**Trustworthy AI** is how we manage those risks with safeguards like data checks, confidence thresholds, human review, and monitoring.
"""
)
