import streamlit as st

st.set_page_config(
    page_title="Trustworthy AI Explained",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Trustworthy AI — Explained")
st.subheader("An overview for decision-makers")

st.markdown(
    """
Welcome to this interactive overview of **Trustworthy AI**.

Use the sidebar to navigate through the topics:

1. **What is Trustworthy AI?** — The five key qualities
2. **Why should we care?** — Public safety, economics and trust
3. **Interactive mini-demo** — See how safeguards change risk in practice
4. **Failure stories** — Real examples of what goes wrong
5. **Roadmap** — Practical steps to get started

---

> *"We don't need perfect AI.  
> We need AI that fails safely, is reviewable, is governed, and earns public trust."*
"""
)
