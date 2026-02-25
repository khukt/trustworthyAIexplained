import streamlit as st
import pandas as pd

from trust_utils import Safeguards, simulate_model_outputs, risk_flags_for_case, overall_risk_summary

st.title("3) Interactive mini-demo: Same AI, different trust level")
st.caption("Toggle safeguards to see how risk changes. This demo uses lightweight simulated outputs to stay simple and portable.")

df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

st.sidebar.header("Safeguards")
s = Safeguards(
    data_quality_checks=st.sidebar.toggle("Data quality checks", value=True),
    bias_check=st.sidebar.toggle("Bias check (fairness)", value=True),
    confidence_threshold=st.sidebar.toggle("Confidence threshold", value=True),
    human_review_low_conf=st.sidebar.toggle("Human review for low confidence", value=True),
)

summary = overall_risk_summary(dfm, s)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Overall risk", summary["overall_risk"])
c2.metric("Risk index (0–1)", summary["risk_index"])
c3.metric("Low-confidence rate", summary["low_conf_rate"])
if summary["quality_incident_rate"] is None:
    c4.metric("Quality incidents", "Not measured")
else:
    c4.metric("Quality incident rate", summary["quality_incident_rate"])

if summary["bias_gap"] is None:
    st.info("Fairness gap not measured (bias check is OFF).")
else:
    st.write(f"**Fairness proxy (gap in positive rate between groups):** {summary['bias_gap']}")

st.divider()

left, right = st.columns([1.1, 1])

with left:
    st.markdown("### Pick a case")
    case_id = st.selectbox("Case ID", dfm["case_id"].tolist(), index=0)
    row = dfm[dfm["case_id"] == case_id].iloc[0]
    flags = risk_flags_for_case(row, s)

    # Decision display (simple)
    decision = "Approve / Support" if row["pred_label"] == 1 else "Reject / No support"

    # Traffic light
    if flags["risk_level"] == "GREEN":
        st.success(f"Risk level: **{flags['risk_level']}**")
    elif flags["risk_level"] == "YELLOW":
        st.warning(f"Risk level: **{flags['risk_level']}**")
    else:
        st.error(f"Risk level: **{flags['risk_level']}**")

    st.metric("AI decision (demo)", decision)
    st.metric("Predicted probability", float(row["pred_prob"]))
    st.metric("Confidence", float(row["confidence"]))
    st.write(f"**Human review required:** {'YES' if flags['needs_review'] else 'NO'}")

    st.markdown("### Why this risk level?")
    for r in flags["reasons"]:
        st.write(f"- {r}")

with right:
    st.markdown("### Case details (what the AI sees)")
    st.dataframe(
        pd.DataFrame([{
            "sector": row["sector"],
            "region": row["region"],
            "data_age_days": int(row["data_age_days"]),
            "missing_rate": float(row["missing_rate"]),
            "ood_score": float(row["ood_score"]),
            "sensitive_group": row["sensitive_group"],
            "need_score": float(row["need_score"]),
        }]),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### “Before vs After” message (for decision makers)")
    st.write(
        """
Even if the AI is “accurate on average”, failures happen.
Safeguards make sure:
- uncertain cases get reviewed,
- data problems are detected,
- fairness risks are measured,
- and decisions remain accountable.
        """
    )

st.divider()
st.markdown("### Quick view: confidence distribution")
st.bar_chart(dfm["confidence"].value_counts(bins=12).sort_index())
