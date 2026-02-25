import streamlit as st

st.title("5) What we recommend (a decision-ready roadmap)")
st.caption("A simple, non-technical roadmap that leaders can act on.")

st.markdown("### Phase A — Minimum safety baseline (quick wins)")
st.write(
    """
- Define **what the AI is for** and **what it is not for**
- Add **confidence thresholds** (do not auto-act on uncertain outputs)
- Add **human review** for low-confidence / high-impact cases
- Basic **data quality** and **data freshness** checks
"""
)

st.markdown("### Phase B — Robust governance")
st.write(
    """
- Monitoring + alerts (detect drift and abnormal behavior)
- Logging and audit trails (who/what/when)
- Roles and accountability (ownership is clear)
- Fairness evaluation, documented and repeated
"""
)

st.markdown("### Phase C — Continuous improvement")
st.write(
    """
- Regular re-evaluation and updates
- Improve data coverage and reduce bias
- Independent review for high-impact uses
- Learning from incidents (like safety engineering)
"""
)

st.divider()
st.markdown("### One slide summary (what to say in a meeting)")
st.success(
    """
We don’t need perfect AI.

We need AI that fails safely, is reviewable, is governed,
and earns public trust.
"""
)
