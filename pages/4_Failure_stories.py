import streamlit as st

st.title("4) Common AI failure stories (and what prevents them)")

stories = [
    {
        "title": "Bias in data → unfair decisions",
        "what_went_wrong": "Historical data reflected unequal treatment; the AI learned and repeated it.",
        "what_prevents": "Fairness checks, representative data, and regular audits."
    },
    {
        "title": "Out-of-date data → wrong recommendations",
        "what_went_wrong": "Reality changed, but the model still used older patterns and assumptions.",
        "what_prevents": "Data freshness checks + monitoring + scheduled re-evaluation."
    },
    {
        "title": "Used outside intended context → unpredictable behavior",
        "what_went_wrong": "AI trained for one setting was deployed in another (new region, new population, new conditions).",
        "what_prevents": "Clear scope documentation + out-of-context detection + human review."
    },
    {
        "title": "No monitoring after deployment → problems discovered too late",
        "what_went_wrong": "Performance drifted silently; errors accumulated before anyone noticed.",
        "what_prevents": "Monitoring, alerts, incident response, and logging/audit trails."
    },
]

for s in stories:
    with st.expander(s["title"], expanded=True):
        st.markdown("**What went wrong:**")
        st.write(s["what_went_wrong"])
        st.markdown("**What prevents it:**")
        st.write(s["what_prevents"])

st.divider()
st.markdown(
    """
### Key takeaway
Most AI incidents are not caused by “evil AI”.

They are caused by **missing safeguards** — the same way accidents happen without safety standards.
"""
)
