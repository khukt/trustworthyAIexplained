import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from trust_utils import Safeguards, simulate_model_outputs, add_risk_columns, case_risk, overall_summary, apply_dark_theme

apply_dark_theme()

st.title("3\ufe0f\u20e3 Interactive Mini-Demo")
st.caption("One clear story that explains: Reliable \u2022 Safe \u2022 Fair \u2022 Transparent \u2022 Accountable")

# ── Data ─────────────────────────────────────────────────────────────────────
df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

# ── Scenario selector ─────────────────────────────────────────────────────────
st.markdown(
    "<div style='background:#eff6ff; border-left:4px solid #2563eb; "
    "border-radius:8px; padding:12px 16px; margin-bottom:12px;'>"
    "<strong style='color:#1e40af;'>📋 Scenario:</strong> "
    "<span style='color:#334155;'>AI helps prioritize cases for support (demo). "
    "The goal is not to replace people — it is to support decisions safely.</span>"
    "</div>",
    unsafe_allow_html=True,
)

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

# ── Case KPI bar ──────────────────────────────────────────────────────────────
st.divider()
k1, k2, k3, k4, k5 = st.columns(5)
decision_label = "Approve \u2705" if row["pred_label"] == 1 else "Reject \u274c"
conf_color = "normal" if row["confidence"] >= 0.65 else "inverse"
k1.metric("AI decision", decision_label)
k2.metric("Confidence", f"{float(row['confidence']):.2f}", delta=f"{'above' if row['confidence'] >= 0.65 else 'below'} threshold")
k3.metric("Need score", f"{float(row['need_score']):.2f}")
k4.metric("Out-of-context", f"{float(row['ood_score']):.2f}")
k5.metric("Data age (days)", int(row["data_age_days"]))

# ── Story navigation ──────────────────────────────────────────────────────────
st.divider()
step_colors = {
    "Reliable": "#22c55e",
    "Safe": "#ef4444",
    "Fair": "#f59e0b",
    "Transparent": "#3b82f6",
    "Accountable": "#a855f7",
}
steps = list(step_colors.keys())
step = st.radio("Story step", steps, horizontal=True)

# Base safeguards
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

# Case snapshot expander
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

active_color = step_colors[step]

# ── Helper: light-themed plotly layout ────────────────────────────────────────
def dark_layout(**kwargs):
    base = dict(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#f8fafc",
        font=dict(color="#334155"),
        legend=dict(font=dict(color="#334155"), bgcolor="#ffffff"),
    )
    base.update(kwargs)
    return base


# ===================================================================
# STEP 1 \u2014 RELIABLE
# ===================================================================
if step == "Reliable":
    st.markdown(
        f"<h3 style='color:{active_color};'>\u2705 Reliable: works consistently and predictably</h3>",
        unsafe_allow_html=True,
    )
    st.write(
        "If we run the *same* case many times, a reliable system should not flip decisions randomly."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        noise = st.slider("Instability (demo)", 0.00, 0.80, 0.20, 0.01,
                          help="Higher = more randomness in the AI output (for illustration).")
        runs = st.slider("Number of runs", 10, 60, 20, 1)
        rng = np.random.default_rng(123)

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
            st.success("\u2705 Reliable: decision stays consistent most of the time.")
        elif stable_rate >= 0.65:
            st.warning("\u26a0\ufe0f Partly reliable: decision changes sometimes \u2014 risky for leadership use.")
        else:
            st.error("\u274c Not reliable: decision flips often \u2014 leaders cannot depend on it.")

    with col2:
        df_plot = pd.DataFrame({
            "Run": np.arange(1, runs + 1),
            "Predicted probability": probs,
            "Decision": labels,
        })
        df_plot["Decision"] = df_plot["Decision"].map({0: "Reject", 1: "Approve"})

        # Colour each point by decision
        fig = px.scatter(
            df_plot, x="Run", y="Predicted probability", color="Decision",
            color_discrete_map={"Approve": "#22c55e", "Reject": "#ef4444"},
            title="Same case, repeated runs (demo)",
        )
        fig.add_hline(y=0.5, line_dash="dash", line_color="#64748b",
                      annotation_text="Decision boundary (0.5)", annotation_font_color="#64748b")
        # Connect with a faint line
        fig.add_trace(go.Scatter(
            x=df_plot["Run"], y=df_plot["Predicted probability"],
            mode="lines", line=dict(color="#334155", width=1),
            showlegend=False,
        ))
        fig.update_layout(**dark_layout(
            yaxis_range=[0, 1],
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            margin=dict(l=10, r=10, t=40, b=10),
        ))
        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "Message for decision makers: **Reliability** means the same input produces consistent outputs. "
            "If a system is unstable, it is not ready for high-impact use."
        )

# ===================================================================
# STEP 2 \u2014 SAFE
# ===================================================================
elif step == "Safe":
    st.markdown(
        f"<h3 style='color:{active_color};'>\U0001f9ef Safe: failures do not create harm</h3>",
        unsafe_allow_html=True,
    )
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
        cr = case_risk(row, s)
        low_conf = row["confidence"] < conf_thr
        out_ctx = row["ood_score"] > ood_thr

        harm_risk = 0
        if auto_decision and (low_conf or out_ctx):
            harm_risk = 2
        elif auto_decision:
            harm_risk = 1
        if human_review and (low_conf or out_ctx):
            harm_risk = max(0, harm_risk - 1)

        decision = "Approve / Support" if row["pred_label"] == 1 else "Reject / No support"
        st.metric("AI suggestion (demo)", decision)
        st.metric("Confidence", float(row["confidence"]))
        st.metric("Out-of-context", float(row["ood_score"]))

        if harm_risk == 0:
            st.success("\u2705 Low harm risk: risky cases are not automatically actioned.")
        elif harm_risk == 1:
            st.warning("\u26a0\ufe0f Medium harm risk: consider stricter thresholds or review.")
        else:
            st.error("\u274c High harm risk: uncertain/out-of-context cases are being automated.")

        st.markdown("**What safe systems do:**")
        for item in ["Use thresholds", "Route risky cases to humans", "Log decisions and monitor issues"]:
            st.markdown(
                f"<div style='background:#f0fdf4; border-left:3px solid #22c55e; "
                f"border-radius:4px; padding:6px 10px; margin:4px 0; color:#166534;'>"
                f"✔️ {item}</div>",
                unsafe_allow_html=True,
            )

    with col2:
        # Quadrant: confidence vs out-of-context with coloured zones
        fig = go.Figure()
        # Background zones
        fig.add_shape(type="rect", x0=0, y0=conf_thr, x1=ood_thr, y1=1,
                      fillcolor="rgba(34,197,94,0.1)", line_width=0)
        fig.add_shape(type="rect", x0=ood_thr, y0=conf_thr, x1=1, y1=1,
                      fillcolor="rgba(245,158,11,0.1)", line_width=0)
        fig.add_shape(type="rect", x0=0, y0=0, x1=ood_thr, y1=conf_thr,
                      fillcolor="rgba(245,158,11,0.1)", line_width=0)
        fig.add_shape(type="rect", x0=ood_thr, y0=0, x1=1, y1=conf_thr,
                      fillcolor="rgba(239,68,68,0.12)", line_width=0)
        # Threshold lines
        fig.add_vline(x=ood_thr, line_dash="dash", line_color="#f59e0b",
                      annotation_text="OOD threshold", annotation_font_color="#f59e0b")
        fig.add_hline(y=conf_thr, line_dash="dash", line_color="#f59e0b",
                      annotation_text="Confidence threshold", annotation_font_color="#f59e0b")
        # This case
        color = "#ef4444" if (low_conf or out_ctx) else "#22c55e"
        fig.add_trace(go.Scatter(
            x=[float(row["ood_score"])],
            y=[float(row["confidence"])],
            mode="markers+text",
            marker=dict(size=18, color=color, symbol="star"),
            text=[row["case_id"]],
            textposition="top center",
            name="This case",
        ))
        fig.update_layout(
            title="Case position vs safety thresholds",
            xaxis=dict(range=[0, 1], title="Out-of-context score", showgrid=False),
            yaxis=dict(range=[0, 1], title="Confidence", showgrid=False),
            **dark_layout(margin=dict(l=10, r=10, t=40, b=10)),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.info(
            "Message for decision makers: **Safe AI** means the system avoids harm by "
            "not automating uncertain or out-of-context cases."
        )

# ===================================================================
# STEP 3 \u2014 FAIR
# ===================================================================
elif step == "Fair":
    st.markdown(
        f"<h3 style='color:{active_color};'>\u2696\ufe0f Fair: decisions are not biased or discriminatory</h3>",
        unsafe_allow_html=True,
    )
    st.write(
        "Fair AI means leaders can *see* whether outcomes differ between groups \u2014 and investigate if they do."
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        fairness_check = st.toggle("Fairness check ON", value=True)
        bias_demo = st.slider("Bias in data (demo)", 0.00, 0.50, 0.10, 0.01,
                              help="This slider simulates how historical bias can affect outcomes.")

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
        bar_colors = ["#3b82f6", "#a855f7"]
        fig = px.bar(
            rates, x="sensitive_group", y="positive_rate",
            title="Positive decision rate by group (demo)",
            color="sensitive_group",
            color_discrete_sequence=bar_colors,
            text=rates["positive_rate"].apply(lambda v: f"{v:.1%}"),
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            yaxis=dict(range=[0, 1.2], showgrid=False, title="Positive rate"),
            xaxis=dict(showgrid=False, title=""),
            showlegend=False,
            **dark_layout(margin=dict(l=10, r=10, t=40, b=10)),
        )
        st.plotly_chart(fig, use_container_width=True)

    # Fairness gauge
    gauge_color = "#ef4444" if gap > 0.15 else ("#f59e0b" if gap > 0.05 else "#22c55e")
    fig_g = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(gap * 100, 1),
        title={"text": "Fairness gap (%)", "font": {"color": "#334155"}},
        gauge={
            "axis": {"range": [0, 50], "tickcolor": "#64748b"},
            "bar": {"color": gauge_color},
            "steps": [
                {"range": [0, 5], "color": "rgba(34,197,94,0.2)"},
                {"range": [5, 15], "color": "rgba(245,158,11,0.2)"},
                {"range": [15, 50], "color": "rgba(239,68,68,0.2)"},
            ],
            "threshold": {"line": {"color": "#334155", "width": 2}, "value": gap * 100},
            "bgcolor": "#f8fafc",
        },
        number={"suffix": "%", "font": {"color": "#1e293b", "size": 30}},
    ))
    fig_g.update_layout(**dark_layout(height=260, margin=dict(l=30, r=30, t=40, b=10)))
    st.plotly_chart(fig_g, use_container_width=True)

    if not fairness_check:
        st.warning("Fairness check is OFF \u2014 leaders may not detect unequal outcomes.")
    else:
        if gap <= 0.05:
            st.success("\u2705 Fairness looks OK in this snapshot (small gap).")
        elif gap <= 0.15:
            st.warning("\u26a0\ufe0f Fairness warning: outcomes differ. Leaders should investigate.")
        else:
            st.error("\u274c Fairness risk: large outcome gap between groups.")

    st.info(
        "Message for decision makers: **Fair AI** requires measuring outcomes across groups. "
        "If differences are large, policy and data must be reviewed."
    )

# ===================================================================
# STEP 4 \u2014 TRANSPARENT
# ===================================================================
elif step == "Transparent":
    st.markdown(
        f"<h3 style='color:{active_color};'>\U0001f50e Transparent: we can explain why a result happened</h3>",
        unsafe_allow_html=True,
    )
    st.write(
        "Transparency here means a **practical explanation** in plain language \u2014 not complex math."
    )

    style = st.radio("Explanation style", ["1 sentence", "3 bullets"], horizontal=True)

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

    col1, col2 = st.columns([1, 1])
    with col1:
        decision_color = "#22c55e" if row["pred_label"] == 1 else "#ef4444"
        st.markdown(
            f"<div style='background:#f8fafc; border:1px solid {decision_color}; "
            f"border-radius:10px; padding:16px 20px; margin-bottom:12px;'>"
            f"<div style='color:#64748b; font-size:0.85rem;'>AI suggestion (demo)</div>"
            f"<div style='color:{decision_color}; font-size:1.4rem; font-weight:700;'>{decision}</div>"
            f"<div style='color:#475569; margin-top:6px;'>Confidence: "
            f"<strong style='color:#1e293b;'>{float(row['confidence']):.2f}</strong></div>"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.subheader("Explanation (plain language)")
        if style == "1 sentence":
            sentence = " ".join(reasons) if reasons else "No major factors stand out in this example."
            st.success(sentence)
        else:
            if not reasons:
                st.success("No major factors stand out in this example.")
            else:
                for r in reasons[:3]:
                    st.markdown(
                        f"<div style='background:#eff6ff; border-left:3px solid #3b82f6; "
                        f"border-radius:4px; padding:8px 12px; margin:4px 0; color:#1e40af;'>"
                        f"• {r}</div>",
                        unsafe_allow_html=True,
                    )

        st.subheader("What would change the decision? (demo)")
        what_if = []
        if row["missing_rate"] > 0.10:
            what_if.append("Reduce missing information \u2192 confidence usually increases.")
        if row["ood_score"] > 0.45:
            what_if.append("If this case is verified as in-scope, risk decreases.")
        if row["data_age_days"] > 60:
            what_if.append("Use fresher data \u2192 improves relevance.")
        if row["need_score"] < 0.55:
            what_if.append("If verified need is higher, the decision may change.")
        if not what_if:
            what_if = ["Changes are likely small for this case in the demo."]
        for w in what_if[:3]:
            st.markdown(
                f"<div style='background:#fffbeb; border-left:3px solid #f59e0b; "
                f"border-radius:4px; padding:8px 12px; margin:4px 0; color:#92400e;'>"
                f"💡 {w}</div>",
                unsafe_allow_html=True,
            )

    with col2:
        factors = pd.DataFrame({
            "Factor": ["Need level", "Missing data", "Out-of-context", "Data age"],
            "Direction (demo)": [
                float(row["need_score"]),
                -float(row["missing_rate"]),
                -float(row["ood_score"]),
                -float(row["data_age_days"] / 180.0),
            ],
        })
        factors["Color"] = factors["Direction (demo)"].apply(lambda v: "#22c55e" if v >= 0 else "#ef4444")
        fig = px.bar(
            factors, x="Direction (demo)", y="Factor", orientation="h",
            title="Key drivers (simplified demo view)",
            color="Direction (demo)",
            color_continuous_scale=["#ef4444", "#94a3b8", "#22c55e"],
            range_color=[-1, 1],
            text="Direction (demo)",
        )
        fig.update_traces(texttemplate="%{x:.2f}", textposition="outside")
        fig.add_vline(x=0, line_color="#64748b")
        fig.update_layout(
            coloraxis_showscale=False,
            xaxis=dict(range=[-1, 1], showgrid=False, title=""),
            yaxis=dict(showgrid=False, title=""),
            **dark_layout(margin=dict(l=10, r=10, t=40, b=10)),
        )
        st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Message for decision makers: **Transparent AI** provides understandable reasons and supports review."
    )

# ===================================================================
# STEP 5 \u2014 ACCOUNTABLE
# ===================================================================
else:
    st.markdown(
        f"<h3 style='color:{active_color};'>\U0001f9fe Accountable: responsibilities, auditing, and governance are clearly defined</h3>",
        unsafe_allow_html=True,
    )
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
        checklist = [
            ("Ownership defined", bool(owner_role)),
            ("Review policy", policy_review),
            ("Audit trail", logging),
            ("Monitoring", monitoring),
        ]
        score = sum(1 for _, v in checklist if v)
        for label, ok in checklist:
            icon = "✅" if ok else "❌"
            color = "#16a34a" if ok else "#dc2626"
            bg = "#f0fdf4" if ok else "#fef2f2"
            border = "#22c55e" if ok else "#ef4444"
            st.markdown(
                f"<div style='background:{bg}; border:1px solid {border}; "
                f"border-radius:8px; padding:8px 14px; margin:4px 0; color:{color};'>"
                f"{icon} {label}</div>",
                unsafe_allow_html=True,
            )

        # Accountability score gauge
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Accountability score", "font": {"color": "#334155"}},
            gauge={
                "axis": {"range": [0, 4], "tickvals": [0, 1, 2, 3, 4], "tickcolor": "#64748b"},
                "bar": {"color": "#a855f7"},
                "steps": [
                    {"range": [0, 2], "color": "rgba(239,68,68,0.2)"},
                    {"range": [2, 3], "color": "rgba(245,158,11,0.2)"},
                    {"range": [3, 4], "color": "rgba(34,197,94,0.2)"},
                ],
                "bgcolor": "#f8fafc",
            },
            number={"suffix": " / 4", "font": {"color": "#1e293b", "size": 30}},
        ))
        fig_g.update_layout(**dark_layout(height=230, margin=dict(l=30, r=30, t=40, b=10)))
        st.plotly_chart(fig_g, use_container_width=True)

    with col2:
        st.subheader("Example audit record (demo)")
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
