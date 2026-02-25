import streamlit as st
import pandas as pd
import plotly.express as px

from trust_utils import Safeguards, simulate_model_outputs, add_risk_columns, overall_summary

st.title("Guided Tour (Presenter mode)")
st.caption("A simple, step-by-step story for politicians and management. Use the tabs below.")

df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

tabs = st.tabs(["1) What", "2) Why", "3) Risks", "4) Safeguards", "5) What to do"])

with tabs[0]:
    st.subheader("What is Trustworthy AI?")
    st.markdown(
        """
**Trustworthy AI** means AI you can **depend on** in real-world decisions.

It focuses on five qualities:
- **Reliable** (works consistently)
- **Safe** (fails without harm)
- **Fair** (no hidden discrimination)
- **Transparent** (reviewable reasons)
- **Accountable** (clear ownership + audit trail)
        """
    )
    st.info("Core message: Trustworthy AI is **risk control** for AI-assisted decisions.")

with tabs[1]:
    st.subheader("Why leaders should care")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.error("Public safety")
        st.write("Wrong recommendation → wrong action → harm and legal consequences.")
    with c2:
        st.warning("Economic / operations")
        st.write("Unreliable AI → inefficiency, downtime, waste.")
    with c3:
        st.info("Trust / legitimacy")
        st.write("Unfair or unexplained decisions → distrust and backlash.")
    st.success("You don’t need perfect AI. You need AI that **fails safely** and is **governed**.")

with tabs[2]:
    st.subheader("What can go wrong (in one picture)")
    st.write("This dataset is a small example of AI-assisted decisions (demo data).")

    # Show relationship between confidence and out-of-context risk
    fig = px.scatter(
        dfm,
        x="ood_score",
        y="confidence",
        color="sector",
        hover_data=["case_id", "region", "missing_rate", "data_age_days", "sensitive_group", "need_score", "pred_prob"],
        title="Uncertain AI tends to appear when cases are out-of-context or data is messy",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
**Interpretation for leaders**
- When cases look *unusual*, AI confidence drops.
- Those are exactly the situations where **automatic decisions are risky**.
        """
    )

with tabs[3]:
    st.subheader("Safeguards reduce risk (what-if)")
    st.write("Use the controls below. Watch how risk distribution changes.")

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown("**Safeguards**")
        data_checks = st.toggle("Data quality checks", True)
        bias_check = st.toggle("Fairness measurement", True)
        conf_on = st.toggle("Confidence threshold", True)
        human_review = st.toggle("Human review for low confidence", True)

    with colB:
        st.markdown("**Policy thresholds**")
        conf_thr = st.slider("Confidence threshold", 0.40, 0.90, 0.65, 0.01)
        missing_thr = st.slider("Missing-data threshold", 0.02, 0.25, 0.10, 0.01)
        ood_thr = st.slider("Out-of-context threshold", 0.10, 0.90, 0.45, 0.01)
        max_age = st.slider("Max data age (days)", 7, 180, 60, 1)

    s = Safeguards(
        data_quality_checks=data_checks,
        bias_check=bias_check,
        confidence_threshold_on=conf_on,
        human_review_low_conf=human_review,
        conf_threshold=conf_thr,
        missing_threshold=missing_thr,
        ood_threshold=ood_thr,
        max_data_age_days=max_age,
    )

    dfv = add_risk_columns(dfm, s)
    kpi = overall_summary(dfm, s)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Overall risk", kpi["overall_risk"])
    k2.metric("Risk index (0–1)", kpi["risk_index"])
    k3.metric("Cases needing review", int(dfv["needs_review"].sum()))
    k4.metric("Low-confidence rate", kpi["low_conf_rate"])

    # Risk distribution
    counts = dfv["risk_level"].value_counts().reindex(["GREEN", "YELLOW", "RED"]).fillna(0).astype(int).reset_index()
    counts.columns = ["risk_level", "count"]
    fig2 = px.bar(counts, x="risk_level", y="count", title="Risk levels across cases (traffic-light view)")
    st.plotly_chart(fig2, use_container_width=True)

    # Fairness view
    if s.bias_check:
        grp = dfm.groupby("sensitive_group")["pred_label"].mean().reset_index()
        grp["positive_rate"] = grp["pred_label"].round(3)
        fig3 = px.bar(grp, x="sensitive_group", y="positive_rate", title="Fairness check: positive decision rate by group")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Fairness measurement is OFF — leaders cannot see whether outcomes differ between groups.")

with tabs[4]:
    st.subheader("What leaders can do (simple roadmap)")
    st.markdown(
        """
**Phase A — Minimum safety baseline**
- define scope (“what the AI is for / not for”)
- confidence threshold + human review
- basic data quality checks

**Phase B — Governance**
- monitoring + alerts
- audit trails (who/what/when)
- fairness checks repeated over time

**Phase C — Continuous improvement**
- periodic re-evaluation
- reduce bias, improve data coverage
- independent review for high-impact uses
        """
    )
    st.success("Closing line: Trustworthy AI helps AI earn **public trust** and prevents **avoidable harm**.")
