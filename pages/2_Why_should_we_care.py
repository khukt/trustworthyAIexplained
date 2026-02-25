import streamlit as st

st.title("2) Why should we care?")
st.markdown(
    """
For decision makers, the question is simple:

**If AI is wrong, who pays the price?**

Trustworthy AI matters because AI failures can create:
- **Public safety risk**
- **Economic/operational risk**
- **Trust & legitimacy risk**
"""
)

st.divider()
c1, c2, c3 = st.columns(3)

with c1:
    st.error("🧍 Public safety risk")
    st.write("Wrong AI recommendation → wrong action → harm, legal consequences.")
with c2:
    st.warning("💶 Economic / operational risk")
    st.write("Unreliable AI → downtime, wasted resources, wrong forecasts or allocations.")
with c3:
    st.info("🗳️ Trust & legitimacy risk")
    st.write("Unfair or unexplained decisions → distrust, backlash, reputation damage.")

st.divider()
st.markdown("### Without vs With Trustworthy AI")

st.table(
    {
        "Without safeguards": [
            "AI used even when uncertain",
            "No clear accountability",
            "Bias remains hidden",
            "Failures discovered too late",
        ],
        "With safeguards": [
            "Confidence thresholds + human review",
            "Defined ownership + audit trail",
            "Fairness checks + documentation",
            "Monitoring + incident response",
        ],
    }
)

st.divider()
st.markdown(
    """
### A useful mindset
We don’t need *perfect* AI.

We need AI that:
- **fails safely**
- is **reviewable**
- is **governed**
- earns **public trust**
"""
)
