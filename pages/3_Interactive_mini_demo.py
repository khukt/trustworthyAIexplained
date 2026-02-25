import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from trust_utils import Safeguards, simulate_model_outputs, add_risk_columns, case_risk

st.title("Interactive mini-demo (story mode)")
st.caption("One clear story that explains: Reliable • Safe • Fair • Transparent • Accountable")

# Load data
df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

# --- TOP: pick scenario + case (kept simple) ---
st.markdown("### Scenario")
st.write("**AI helps prioritize cases for support** (demo). The goal is not to replace people — it is to support decisions safely.")

colA, colB, colC = st.columns([1, 1, 1.2])
with colA:
    sector = st.selectbox("Sector", sorted(dfm["sector"].unique()))
with colB:
    region = st.selectbox("Region", sorted(dfm["region"].unique()))
df_f = dfm[(dfm["sector"] == sector) & (dfm["region"] == region)].copy()
if df_f.empty:
    st.warning("No cases found for this filter (demo data). Try another sector/region.")
    st.stop()

with colC:
    case_id = st.selectbox("Pick one case (example)", df_f["case_id"].tolist(), index=0)

row = df_f[df_f["case_id"] == case_id].iloc[0]

st.divider()

# --- STORY NAV ---
steps = ["Reliable", "Safe", "Fair", "Transparent", "Accountable"]
step = st.radio("Story step", steps, horizontal=True)

# Keep safeguards object for thresholds (used in Safe + Case risk)
# (We keep them visible only where they matter, to avoid complexity.)
base_s = Safeguards(
    data_quality_checks=True,
    bias_check=True,
    confidence_threshold_on=True,
    human_review_low_conf=True,
    conf_threshold=0.65,
    missing_threshold=0.10,
    ood_threshold=0.45,
    max_data_age_days=60,
)

# Common small case card (always visible)
with st.expander("Case snapshot (what we know about this case)", expanded=False):
    snap = pd.DataFrame([{
        "case_id": row["case_id"],
        "sector": row["sector"],
        "region": row["region"],
        "need_score (demo)": float(row["need_score"]),
        "confidence": float(row["confidence"]),
        "out-of-context": float(row["ood_score"]),
        "missing_rate": float(row["missing_rate"]),
        "data_age_days": int(row["data_age_days"]),
        "group (demo)": row["sensitive_group"],
    }])
    st.dataframe(snap, use_container_width=True, hide_index=True)

# -------------------------------------------------------------------
# STEP 1 — RELIABLE
# -------------------------------------------------------------------
if step == "Reliable":
    st.header("Reliable: works consistently and predictably")
    st.write(
        "If we run the *same* case many times, a reliable system should not flip decisions randomly."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        noise = st.slider("Instability (demo)", 0.00, 0.80, 0.20, 0.01,
                          help="Higher = more randomness in the AI output (for illustration).")
        runs = st.slider("Number of runs", 10, 60, 20, 1)
        rng = np.random.default_rng(123)

        # Simulate repeated outputs
        base_prob = float(row["pred_prob"])
        probs = np.clip(base_prob + rng.normal(0, noise, size=runs), 0, 1)
        labels = (probs >= 0.5).astype(int)

        stable_rate = float(np.mean(labels == labels[0]))
        flips = int(np.sum(labels != labels[0]))

        decision0 = "Approve" if labels[0] == 1 else "Reject"
        st.metric("Initial decision", decision0)
        st.metric("Flips (out of runs)", f"{flips} / {runs}")
        st.metric("Stability rate", f"{stable_rate:.2f}")

        if stable_rate >= 0.85:
            st.success("✅ Reliable: decision stays consistent most of the time.")
        elif stable_rate >= 0.65:
            st.warning("⚠️ Partly reliable: decision changes sometimes — risky for leadership use.")
        else:
            st.error("❌ Not reliable: decision flips often — leaders cannot depend on it.")

    with col2:
        df_plot = pd.DataFrame({"Run": np.arange(1, runs + 1), "Predicted probability": probs, "Decision": labels})
        df_plot["Decision"] = df_plot["Decision"].map({0: "Reject", 1: "Approve"})
        fig = px.line(df_plot, x="Run", y="Predicted probability", title="Same case, repeated runs (demo)")
        fig.update_layout(yaxis_range=[0, 1])
        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "Message for decision makers: **Reliability** means the same input produces consistent outputs. "
            "If a system is unstable, it is not ready for high-impact use."
        )

# -------------------------------------------------------------------
# STEP 2 — SAFE
# -------------------------------------------------------------------
elif step == "Safe":
    st.header("Safe: failures do not create harm")
    st.write(
        "Safe AI does **not** automatically act when the system is uncertain or the case is out-of-context."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        auto_decision = st.toggle("Auto-decision allowed?", value=False,
                                  help="If ON, the system automatically applies the AI decision.")
        human_review = st.toggle("Human review for risky cases?", value=True,
                                 help="If ON, low-confidence cases are routed to a human reviewer.")
        conf_thr = st.slider("Confidence threshold", 0.40, 0.90, 0.65, 0.01)
        ood_thr = st.slider("Out-of-context threshold", 0.10, 0.90, 0.45, 0.01)

        s = Safeguards(
            data_quality_checks=True,
            bias_check=True,
            confidence_threshold_on=True,
            human_review_low_conf=human_review,
            conf_threshold=conf_thr,
            missing_threshold=0.10,
            ood_threshold=ood_thr,
            max_data_age_days=60,
        )

        # Evaluate this case
        cr = case_risk(row, s)
        low_conf = row["confidence"] < conf_thr
        out_ctx = row["ood_score"] > ood_thr

        harm_risk = 0
        if auto_decision and (low_conf or out_ctx):
            harm_risk = 2
        elif auto_decision:
            harm_risk = 1
        else:
            harm_risk = 0
        # human review reduces harm risk
        if human_review and (low_conf or out_ctx):
            harm_risk = max(0, harm_risk - 1)

        decision = "Approve / Support" if row["pred_label"] == 1 else "Reject / No support"
        st.metric("AI suggestion (demo)", decision)
        st.metric("Confidence", float(row["confidence"]))
        st.metric("Out-of-context", float(row["ood_score"]))

        if harm_risk == 0:
            st.success("✅ Low harm risk: risky cases are not automatically actioned.")
        elif harm_risk == 1:
            st.warning("⚠️ Medium harm risk: consider stricter thresholds or review.")
        else:
            st.error("❌ High harm risk: uncertain/out-of-context cases are being automated.")

        st.markdown("**What safe systems do:**")
        st.write("- Use thresholds")
        st.write("- Route risky cases to humans")
        st.write("- Log decisions and monitor issues")

    with col2:
        # Show where the case sits vs thresholds
        mark = pd.DataFrame([{
            "case": row["case_id"],
            "confidence": float(row["confidence"]),
            "out_of_context": float(row["ood_score"]),
        }])
        fig = px.scatter(
            mark, x="out_of_context", y="confidence",
            title="This case vs safety thresholds"
        )
        fig.add_vline(x=ood_thr, line_dash="dash")
        fig.add_hline(y=conf_thr, line_dash="dash")
        fig.update_layout(xaxis_range=[0,1], yaxis_range=[0,1])
        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "Message for decision makers: **Safe AI** means the system avoids harm by "
            "not automating uncertain or out-of-context cases."
        )

# -------------------------------------------------------------------
# STEP 3 — FAIR
# -------------------------------------------------------------------
elif step == "Fair":
    st.header("Fair: decisions are not biased or discriminatory")
    st.write(
        "Fair AI means leaders can *see* whether outcomes differ between groups — and investigate if they do."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        fairness_check = st.toggle("Fairness check ON", value=True)
        bias_demo = st.slider("Bias in data (demo)", 0.00, 0.50, 0.10, 0.01,
                              help="This slider simulates how historical bias can affect outcomes.")

    # Build a demo-biased prediction by shifting probability for one group
    df2 = df_f.copy()
    df2["pred_prob_biased"] = df2["pred_prob"]
    df2.loc[df2["sensitive_group"] == "Group B", "pred_prob_biased"] = np.clip(
        df2.loc[df2["sensitive_group"] == "Group B", "pred_prob_biased"] - bias_demo, 0, 1
    )
    df2["pred_label_biased"] = (df2["pred_prob_biased"] >= 0.5).astype(int)

    rates = df2.groupby("sensitive_group")["pred_label_biased"].mean().reset_index()
    rates.rename(columns={"pred_label_biased": "positive_rate"}, inplace=True)
    gap = float(rates["positive_rate"].max() - rates["positive_rate"].min())

    with col2:
        fig = px.bar(rates, x="sensitive_group", y="positive_rate", title="Positive decision rate by group (demo)")
        fig.update_layout(yaxis_range=[0, 1])
        st.plotly_chart(fig, use_container_width=True)

    st.metric("Fairness gap (max-min)", round(gap, 3))
    if not fairness_check:
        st.warning("Fairness check is OFF — leaders may not detect unequal outcomes.")
    else:
        if gap <= 0.05:
            st.success("✅ Fairness looks OK in this snapshot (small gap).")
        elif gap <= 0.15:
            st.warning("⚠️ Fairness warning: outcomes differ. Leaders should investigate.")
        else:
            st.error("❌ Fairness risk: large outcome gap between groups.")

    st.info(
        "Message for decision makers: **Fair AI** requires measuring outcomes across groups. "
        "If differences are large, policy and data must be reviewed."
    )

# -------------------------------------------------------------------
# STEP 4 — TRANSPARENT
# -------------------------------------------------------------------
elif step == "Transparent":
    st.header("Transparent: we can explain why a result happened")
    st.write(
        "Transparency here means a **practical explanation** in plain language — not complex math."
    )

    style = st.radio("Explanation style", ["1 sentence", "3 bullets"], horizontal=True)

    # Simple, honest reasons (not SHAP)
    reasons = []
    if row["need_score"] >= 0.65:
        reasons.append("Need level is high.")
    elif row["need_score"] <= 0.45:
        reasons.append("Need level is moderate/low.")
    if row["missing_rate"] > 0.10:
        reasons.append("Some required information is missing.")
    if row["ood_score"] > 0.45:
        reasons.append("Case looks unusual compared to typical cases.")
    if row["data_age_days"] > 60:
        reasons.append("Data may be outdated.")

    decision = "Approve / Support" if row["pred_label"] == 1 else "Reject / No support"

    st.subheader("AI suggestion (demo)")
    st.write(f"**Decision:** {decision}")
    st.write(f"**Confidence:** {float(row['confidence']):.2f}")

    st.subheader("Explanation (plain language)")
    if style == "1 sentence":
        sentence = " ".join(reasons) if reasons else "No major factors stand out in this example."
        st.success(sentence)
    else:
        if not reasons:
            st.success("No major factors stand out in this example.")
        else:
            for r in reasons[:3]:
                st.write(f"- {r}")

    # What would change?
    st.subheader("What would change the decision? (demo)")
    what_if = []
    if row["missing_rate"] > 0.10:
        what_if.append("Reduce missing information → confidence usually increases.")
    if row["ood_score"] > 0.45:
        what_if.append("If this case is verified as in-scope (not out-of-context), risk decreases.")
    if row["data_age_days"] > 60:
        what_if.append("Use fresher data → improves relevance.")
    if row["need_score"] < 0.55:
        what_if.append("If verified need is higher, the decision may change.")
    if not what_if:
        what_if = ["Changes are likely small for this case in the demo."]

    for w in what_if[:3]:
        st.write(f"- {w}")

    # Visual: simple factor bars
    factors = pd.DataFrame({
        "Factor": ["Need level", "Missing data", "Out-of-context", "Data age"],
        "Direction (demo)": [
            float(row["need_score"]),
            -float(row["missing_rate"]),
            -float(row["ood_score"]),
            -float(row["data_age_days"] / 180.0),
        ],
    })
    fig = px.bar(factors, x="Direction (demo)", y="Factor", orientation="h", title="Key drivers (simplified demo view)")
    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Message for decision makers: **Transparent AI** provides understandable reasons and supports review."
    )

# -------------------------------------------------------------------
# STEP 5 — ACCOUNTABLE
# -------------------------------------------------------------------
else:
    st.header("Accountable: responsibilities, auditing, and governance are clearly defined")
    st.write(
        "Accountability means we can answer: **who owned the decision, what controls were applied, and how it can be audited**."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        owner_role = st.selectbox("Decision owner (role)", ["Unit manager", "Agency director", "Case officer", "Project lead"])
        policy_review = st.toggle("Review policy enabled", value=True)
        logging = st.toggle("Logging / audit trail enabled", value=True)
        monitoring = st.toggle("Monitoring planned", value=True)

        st.subheader("Accountability checklist")
        st.write(f"- Ownership defined: {'✅' if owner_role else '❌'}")
        st.write(f"- Review policy: {'✅' if policy_review else '❌'}")
        st.write(f"- Audit trail: {'✅' if logging else '❌'}")
        st.write(f"- Monitoring: {'✅' if monitoring else '❌'}")

    with col2:
        st.subheader("Example audit record (demo)")
        # Make a simple audit entry
        audit = {
            "case_id": row["case_id"],
            "sector": row["sector"],
            "region": row["region"],
            "ai_decision": "Approve" if row["pred_label"] == 1 else "Reject",
            "pred_prob": float(row["pred_prob"]),
            "confidence": float(row["confidence"]),
            "out_of_context": float(row["ood_score"]),
            "owner_role": owner_role,
            "review_policy": policy_review,
            "logging": logging,
            "monitoring": monitoring,
        }
        st.json(audit)

        st.info(
            "Message for decision makers: **Accountable AI** creates traceable decisions and clear responsibility."
        )

st.divider()
st.caption("This demo uses simulated outputs and simplified indicators to make the policy story clear and portable.")
