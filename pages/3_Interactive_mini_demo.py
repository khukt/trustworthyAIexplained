import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from trust_utils import Safeguards, simulate_model_outputs, add_risk_columns, case_risk, overall_summary

st.title("Interactive mini-demo (dashboard + what-if controls)")
st.caption("Explore cases, adjust safeguards, and see immediate changes in risk, review load, and fairness indicators.")

# Load data
df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

# Sidebar: audience-friendly controls
st.sidebar.header("1) Filter the scenario")
sector = st.sidebar.multiselect("Sector", sorted(dfm["sector"].unique()), default=sorted(dfm["sector"].unique()))
region = st.sidebar.multiselect("Region", sorted(dfm["region"].unique()), default=sorted(dfm["region"].unique()))

dfm_f = dfm[dfm["sector"].isin(sector) & dfm["region"].isin(region)].copy()

st.sidebar.header("2) Safeguards (policy knobs)")
data_checks = st.sidebar.toggle("Data quality checks", True)
bias_check = st.sidebar.toggle("Fairness measurement", True)
conf_on = st.sidebar.toggle("Confidence threshold", True)
human_review = st.sidebar.toggle("Human review for low confidence", True)

st.sidebar.header("3) Thresholds (interactive)")
conf_thr = st.sidebar.slider("Confidence threshold", 0.40, 0.90, 0.65, 0.01)
missing_thr = st.sidebar.slider("Missing-data threshold", 0.02, 0.25, 0.10, 0.01)
ood_thr = st.sidebar.slider("Out-of-context threshold", 0.10, 0.90, 0.45, 0.01)
max_age = st.sidebar.slider("Max data age (days)", 7, 180, 60, 1)

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

# Compute dashboard columns
dfv = add_risk_columns(dfm_f, s)
kpi = overall_summary(dfm_f, s)

# Top KPIs
k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Overall risk", kpi["overall_risk"])
k2.metric("Risk index (0–1)", kpi["risk_index"])
k3.metric("Cases", len(dfm_f))
k4.metric("Needs human review", int(dfv["needs_review"].sum()))
k5.metric("Low-confidence rate", kpi["low_conf_rate"])

st.divider()

tabA, tabB, tabC = st.tabs(["Dashboard", "Case explorer", "Fairness & accountability"])

with tabA:
    c1, c2 = st.columns([1.1, 1])

    with c1:
        # Risk distribution
        counts = dfv["risk_level"].value_counts().reindex(["GREEN", "YELLOW", "RED"]).fillna(0).astype(int).reset_index()
        counts.columns = ["risk_level", "count"]
        fig = px.bar(counts, x="risk_level", y="count", title="Traffic-light risk distribution")
        st.plotly_chart(fig, use_container_width=True)

        # Review load over confidence
        df_hist = dfv.copy()
        df_hist["conf_bin"] = pd.cut(df_hist["confidence"], bins=12)
        hist = df_hist.groupby("conf_bin")["needs_review"].sum().reset_index()
        hist["conf_bin"] = hist["conf_bin"].astype(str)
        fig2 = px.bar(hist, x="conf_bin", y="needs_review", title="How many cases require human review (by confidence band)")
        fig2.update_layout(xaxis_title="Confidence band", yaxis_title="Cases needing review")
        st.plotly_chart(fig2, use_container_width=True)

    with c2:
        # Scatter: OOD vs confidence
        fig3 = px.scatter(
            dfv,
            x="ood_score",
            y="confidence",
            color="risk_level",
            hover_data=["case_id", "sector", "region", "missing_rate", "data_age_days", "sensitive_group", "need_score", "pred_prob"],
            title="Risk often increases when cases are out-of-context and low-confidence",
        )
        st.plotly_chart(fig3, use_container_width=True)

        # Quality flags
        flags = pd.DataFrame({
            "Flag": ["Data quality", "Stale data", "Out-of-context", "Low confidence"],
            "Cases": [
                int(dfv["flag_quality"].sum()),
                int(dfv["flag_stale"].sum()),
                int(dfv["flag_ood"].sum()),
                int(dfv["flag_low_conf"].sum()),
            ],
        })
        fig4 = px.bar(flags, x="Flag", y="Cases", title="What is triggering risk?")
        st.plotly_chart(fig4, use_container_width=True)

    st.info(
        "Presenter line: *This is why we use safeguards — not because AI is bad, but because uncertainty and out-of-context cases are unavoidable.*"
    )

with tabB:
    st.subheader("Pick a case and see a plain-language explanation")

    case_id = st.selectbox("Case ID", dfv["case_id"].tolist(), index=0)
    row = dfv[dfv["case_id"] == case_id].iloc[0]
    cr = case_risk(row, s)

    left, right = st.columns([1.1, 1])
    with left:
        # Traffic light
        if cr["risk_level"] == "GREEN":
            st.success(f"Risk level: **{cr['risk_level']}**")
        elif cr["risk_level"] == "YELLOW":
            st.warning(f"Risk level: **{cr['risk_level']}**")
        else:
            st.error(f"Risk level: **{cr['risk_level']}**")

        decision = "Approve / Support" if row["pred_label"] == 1 else "Reject / No support"
        st.metric("AI decision (demo)", decision)
        st.metric("Predicted probability", float(row["pred_prob"]))
        st.metric("Confidence", float(row["confidence"]))
        st.write(f"**Human review required:** {'YES' if cr['needs_review'] else 'NO'}")

        st.markdown("### Why?")
        for r in cr["reasons"]:
            st.write(f"- {r}")

    with right:
        st.markdown("### Case details")
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

        # Explainable "contribution" bars (simple and honest: not real SHAP)
        contrib = pd.DataFrame({
            "Factor": ["Need level", "Missing data", "Out-of-context", "Data age"],
            "Effect (demo)": [
                float(row["need_score"]),
                -float(row["missing_rate"]),
                -float(row["ood_score"]),
                -float(row["data_age_days"] / 180.0),
            ],
        })
        fig = px.bar(contrib, x="Effect (demo)", y="Factor", orientation="h", title="Simple explanation (demo factors)")
        st.plotly_chart(fig, use_container_width=True)

    st.caption("Note: explanations here are simplified to be understandable in a policy discussion.")

with tabC:
    st.subheader("Fairness & accountability view")

    c1, c2 = st.columns([1, 1])

    with c1:
        if s.bias_check:
            grp = dfv.groupby("sensitive_group")["pred_label"].mean().reset_index()
            grp["positive_rate"] = grp["pred_label"].round(3)
            fig = px.bar(grp, x="sensitive_group", y="positive_rate", title="Positive decision rate by group (fairness proxy)")
            st.plotly_chart(fig, use_container_width=True)

            gap = float(grp["positive_rate"].max() - grp["positive_rate"].min())
            st.metric("Fairness gap (max-min)", round(gap, 3))
            st.write("If this gap is large, leaders should ask: *why are outcomes different?*")
        else:
            st.warning("Fairness measurement is OFF — differences between groups may remain invisible.")

    with c2:
        st.markdown("### Accountability checklist (demo)")
        st.checkbox("AI scope documented (what it is / is not for)", value=True, disabled=True)
        st.checkbox("Confidence threshold policy defined", value=s.confidence_threshold_on, disabled=True)
        st.checkbox("Human review for uncertain cases", value=s.human_review_low_conf, disabled=True)
        st.checkbox("Data quality checks applied", value=s.data_quality_checks, disabled=True)
        st.checkbox("Monitoring & audits planned", value=True, disabled=True)

        st.info(
            "Presenter line: *Accountability means we can answer: who owns it, how decisions were made, and how problems are handled.*"
        )

st.divider()
with st.expander("Download the filtered dataset (for slides / meetings)"):
    st.download_button(
        "Download CSV",
        dfv.to_csv(index=False).encode("utf-8"),
        file_name="trustworthy_ai_demo_filtered.csv",
        mime="text/csv",
    )
