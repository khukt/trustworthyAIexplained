import streamlit as st

st.title("1) What is Trustworthy AI?")
st.markdown(
    """
Trustworthy AI is AI that is **reliable**, **safe**, **fair**, **transparent**, and **accountable** — designed to earn and maintain human trust across real-world applications.

It focuses on five practical qualities:

- **Reliable**: works consistently and predictably
- **Safe**: failures do not create harm
- **Fair**: decisions are not biased or discriminatory
- **Transparent**: we can explain *why* a result happened (at least at a practical level)
- **Accountable**: responsibilities, auditing, and governance are clearly defined
"""
)

st.divider()

cols = st.columns(5)
items = [
    ("✅ Reliable", "Stable performance, not random behavior."),
    ("🧯 Safe", "Fail-safe rules and guardrails reduce harm."),
    ("⚖️ Fair", "Checks reduce discriminatory outcomes."),
    ("🔎 Transparent", "Decision reasoning is explainable and reviewable."),
    ("🧾 Accountable", "Logs, audits, and ownership are defined."),
]
for c, (h, t) in zip(cols, items):
    with c:
        st.markdown(f"### {h}")
        st.caption(t)

st.divider()
st.markdown(
    """
### What Trustworthy AI is *not*
- Not a “luxury feature”
- Not only about accuracy
- Not about replacing people

**It is risk management** for AI-assisted decisions.
"""
)
