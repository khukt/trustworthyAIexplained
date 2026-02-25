import streamlit as st

st.set_page_config(
    page_title="Trustworthy AI — Overview Demo",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ Trustworthy AI — Overview Demo")
st.caption("A step-by-step, politician- and management-friendly demo: what it is, why it matters, and how safeguards reduce risk.")

st.success("Start here: open **Guided Tour** in the left menu (presenter mode).")

col1, col2 = st.columns([1.25, 1])
with col1:
    st.markdown(
        """
### The main idea
**Trustworthy AI** is AI that is **reliable, safe, fair, transparent, and accountable**.

For leaders, it's not a technical detail — it's **risk management**:
- reduce harmful mistakes,
- prevent unfair outcomes,
- keep public trust,
- and make accountability clear.

### What you’ll see in this demo
- A short guided story (**Guided Tour**)
- A rich dashboard (**Interactive mini-demo**) with *what-if* controls
- Realistic failure stories + a practical roadmap
        """
    )

with col2:
    st.info(
        """
**Tip for presentations**
Use the **Guided Tour** page to walk the audience through the story in 5–7 minutes.
        """
    )
    st.markdown("### Quick glossary")
    st.write("- **Confidence**: how sure the AI is about its output.")
    st.write("- **Out-of-context**: cases unlike what the AI has seen before.")
    st.write("- **Fairness gap**: difference in outcomes between groups (a warning sign).")

st.divider()
st.markdown(
    """
### Why this matters
AI can be helpful — but when it fails, the cost is often **public safety**, **money**, and **trust**.

Safeguards help AI **fail safely** and keep decisions **reviewable**.
"""
)
