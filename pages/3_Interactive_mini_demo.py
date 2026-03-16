import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from trust_utils import (
    Safeguards,
    add_risk_columns,
    case_risk,
    material_icon,
    overall_summary,
    render_callout,
    render_page_header,
    render_section_intro,
    setup_page,
    simulate_model_outputs,
)


setup_page("demo", "Interactive Mini-Demo")

render_page_header(
    title="Interactive Mini-Demo",
    subtitle="A simpler walkthrough showing how the same AI system behaves with and without safeguards.",
    icon_name="tune",
    accent="#0f766e",
    chips=["One case", "One comparison", "Five trust checks", "Decision-maker friendly"],
    eyebrow="Live walkthrough",
)

render_callout(
    title="How to use this demo",
    body="Pick a case, compare an unsafe setup with a safeguarded setup, then open the trust-dimension tabs if you want a deeper explanation.",
    icon_name="map",
    accent="#1d4ed8",
)

df = pd.read_csv("data/sample_cases.csv")
dfm = simulate_model_outputs(df)

render_section_intro(
    title="1. Pick a case",
    body="The scenario is intentionally simple: AI helps prioritize cases for support. The goal is to support people, not replace them.",
    icon_name="assignment",
)

filter_a, filter_b, filter_c = st.columns([1, 1, 1.2], gap="large")
with filter_a:
    sector = st.selectbox("Sector", sorted(dfm["sector"].unique()))
with filter_b:
    region = st.selectbox("Region", sorted(dfm["region"].unique()))

df_f = dfm[(dfm["sector"] == sector) & (dfm["region"] == region)].copy()
if df_f.empty:
    st.warning("No cases found for this filter in the demo data. Try another sector or region.")
    st.stop()

default_order = add_risk_columns(df_f, Safeguards()).sort_values(
    by=["risk_points", "confidence"], ascending=[False, True]
)
case_options = default_order["case_id"].tolist()
with filter_c:
    case_id = st.selectbox("Case", case_options, index=0)

row = df_f[df_f["case_id"] == case_id].iloc[0]

snapshot_left, snapshot_right = st.columns([1.05, 0.95], gap="large")

with snapshot_left:
    st.markdown(
        (
            '<div class="demo-case-card">'
            '<div class="demo-case-kicker">Selected case</div>'
            f'<div class="demo-case-title">Case {row["case_id"]} in {row["sector"]} / {row["region"]}</div>'
            '<div class="demo-case-copy">'
            "The model estimates whether this case should be prioritized for support. In the demo, the AI output depends on need score, data quality, whether the case looks unusual, and how old the data is."
            "</div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )

    metric_a, metric_b, metric_c = st.columns(3, gap="small")
    with metric_a:
        st.metric("AI suggestion", "Support" if row["pred_label"] == 1 else "No support")
    with metric_b:
        st.metric("Confidence", f"{float(row['confidence']):.2f}")
    with metric_c:
        st.metric("Need score", f"{float(row['need_score']):.2f}")

with snapshot_right:
    signals = []
    if row["ood_score"] > 0.45:
        signals.append(("This case looks unusual compared with the cases the model usually sees.", "#f59e0b"))
    if row["missing_rate"] > 0.10:
        signals.append(("Some important information is missing.", "#ef4444"))
    if row["data_age_days"] > 60:
        signals.append(("The data is old enough that the situation may have changed.", "#7c3aed"))
    if not signals:
        signals.append(("No major warning flags stand out immediately, but safeguards still matter.", "#16a34a"))

    signal_html = "".join(
        (
            '<div class="demo-signal">'
            f'<span class="demo-signal-dot" style="background:{color};"></span>'
            f'<div class="demo-signal-copy">{copy}</div>'
            "</div>"
        )
        for copy, color in signals
    )
    st.markdown(
        (
            '<div class="demo-case-card">'
            '<div class="demo-case-kicker">What makes this case easy or hard</div>'
            '<div class="demo-signal-list">'
            f"{signal_html}"
            "</div>"
            "</div>"
        ),
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="2. Compare two ways to use the same AI",
    body="The easiest way to understand trustworthy AI is to compare the same case under a weak setup and a safer setup.",
    icon_name="compare_arrows",
)

control_left, control_right = st.columns([0.95, 1.05], gap="large")

with control_left:
    st.markdown(
        """
        <div class="card">
          <div class="card-title">Safeguarded setup</div>
          <div class="card-desc">
            Adjust a few controls and see how the safer setup changes the outcome for the same case and the same filtered cohort.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    conf_thr = st.slider("Confidence threshold", 0.40, 0.90, 0.65, 0.01)
    ood_thr = st.slider("Out-of-context threshold", 0.10, 0.90, 0.45, 0.01)
    max_age = st.slider("Maximum data age (days)", 30, 120, 60, 5)
    human_review = st.toggle("Route low-confidence cases to human review", value=True)
    data_checks = st.toggle("Use data-quality checks", value=True)

unsafe_s = Safeguards(
    data_quality_checks=False,
    bias_check=False,
    confidence_threshold_on=False,
    human_review_low_conf=False,
    conf_threshold=conf_thr,
    missing_threshold=0.10,
    ood_threshold=ood_thr,
    max_data_age_days=max_age,
)
safe_s = Safeguards(
    data_quality_checks=data_checks,
    bias_check=True,
    confidence_threshold_on=True,
    human_review_low_conf=human_review,
    conf_threshold=conf_thr,
    missing_threshold=0.10,
    ood_threshold=ood_thr,
    max_data_age_days=max_age,
)

unsafe_case = case_risk(row, unsafe_s)
safe_case = case_risk(row, safe_s)


def risk_pill(level: str) -> str:
    if level == "GREEN":
        return '<span class="demo-pill demo-pill-green">Low risk</span>'
    if level == "YELLOW":
        return '<span class="demo-pill demo-pill-yellow">Medium risk</span>'
    return '<span class="demo-pill demo-pill-red">High risk</span>'


def decision_path(risk: dict, safeguarded: bool) -> str:
    if not safeguarded:
        return "The AI output is used directly, even when the case is uncertain."
    if risk["needs_review"]:
        return "The case is routed to a human before any action is taken."
    if risk["risk_level"] == "RED":
        return "The case should not be actioned automatically under this setup."
    return "The case can proceed with the configured safeguards in place."


def reason_html(reasons: list[str]) -> str:
    return "".join(f'<div class="demo-reason">{reason}</div>' for reason in reasons[:4])


with control_right:
    compare_a, compare_b = st.columns(2, gap="large")
    with compare_a:
        st.markdown(
            (
                '<div class="demo-outcome-card demo-outcome-card-risky">'
                '<div class="demo-outcome-kicker">Without safeguards</div>'
                '<div class="demo-outcome-title">Weak governance setup</div>'
                f"{risk_pill(unsafe_case['risk_level'])}"
                f'<div class="demo-outcome-copy">{decision_path(unsafe_case, safeguarded=False)}</div>'
                '<div class="demo-reason-list">'
                f"{reason_html(unsafe_case['reasons'])}"
                "</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )
    with compare_b:
        st.markdown(
            (
                '<div class="demo-outcome-card demo-outcome-card-good">'
                '<div class="demo-outcome-kicker">With safeguards</div>'
                '<div class="demo-outcome-title">Safer operational setup</div>'
                f"{risk_pill(safe_case['risk_level'])}"
                f'<div class="demo-outcome-copy">{decision_path(safe_case, safeguarded=True)}</div>'
                '<div class="demo-reason-list">'
                f"{reason_html(safe_case['reasons'])}"
                "</div>"
                "</div>"
            ),
            unsafe_allow_html=True,
        )

st.markdown(
    (
        '<div class="demo-note">'
        "<strong>Main takeaway:</strong> The same model output can become much safer when uncertain, stale, or unusual cases are slowed down, checked, and reviewed."
        "</div>"
    ),
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="3. What changes across the filtered cases",
    body="The selected case is one example. This chart shows what the setup does to all cases in the current sector and region.",
    icon_name="bar_chart",
)

unsafe_df = add_risk_columns(df_f, unsafe_s)
safe_df = add_risk_columns(df_f, safe_s)
unsafe_summary = overall_summary(unsafe_df, unsafe_s)
safe_summary = overall_summary(safe_df, safe_s)

summary_a, summary_b, summary_c, summary_d = st.columns(4, gap="small")
with summary_a:
    st.metric("Unsafe: risky cases", int((unsafe_df["risk_level"] != "GREEN").sum()))
with summary_b:
    st.metric("Safeguarded: risky cases", int((safe_df["risk_level"] != "GREEN").sum()))
with summary_c:
    st.metric("Safeguarded: review cases", int(safe_df["needs_review"].sum()))
with summary_d:
    st.metric("Fairness gap (demo)", f"{(safe_summary['bias_gap'] or 0):.2f}")

risk_counts = pd.concat(
    [
        unsafe_df["risk_level"].value_counts().rename("count").reset_index().assign(mode="Without safeguards"),
        safe_df["risk_level"].value_counts().rename("count").reset_index().assign(mode="With safeguards"),
    ],
    ignore_index=True,
)
risk_counts.rename(columns={"index": "risk_level"}, inplace=True)
risk_counts["risk_level"] = pd.Categorical(risk_counts["risk_level"], categories=["GREEN", "YELLOW", "RED"], ordered=True)
risk_counts = risk_counts.sort_values(["mode", "risk_level"])

fig_counts = px.bar(
    risk_counts,
    x="risk_level",
    y="count",
    color="mode",
    barmode="group",
    color_discrete_map={"Without safeguards": "#f59e0b", "With safeguards": "#0f766e"},
    labels={"risk_level": "Risk level", "count": "Number of cases", "mode": ""},
)
fig_counts.update_layout(
    paper_bgcolor="rgba(255,255,255,0)",
    plot_bgcolor="rgba(255,255,255,0)",
    font=dict(color="#334155"),
    margin=dict(l=10, r=10, t=20, b=10),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    yaxis=dict(gridcolor="#e2e8f0"),
)
st.plotly_chart(fig_counts, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

render_section_intro(
    title="4. Understand the five trust dimensions",
    body="Use these tabs if you want to connect the comparison above to the five ideas used across the rest of the app.",
    icon_name="tabs",
)

reasons = []
if row["need_score"] >= 0.65:
    reasons.append("Need level is high.")
elif row["need_score"] <= 0.45:
    reasons.append("Need level is lower or uncertain.")
if row["missing_rate"] > 0.10:
    reasons.append("Some required information is missing.")
if row["ood_score"] > safe_s.ood_threshold:
    reasons.append("The case looks unusual compared with typical examples.")
if row["data_age_days"] > safe_s.max_data_age_days:
    reasons.append("The data may be too old.")
if not reasons:
    reasons = ["No major warning signs stand out in this case."]

tabs = st.tabs(["Reliable", "Safe", "Fair", "Transparent", "Accountable"])

with tabs[0]:
    st.markdown("**Reliable means the same case should not flip unpredictably.**")
    instability = st.slider("Instability (demo)", 0.00, 0.80, 0.20, 0.01, key="demo_reliability")
    runs = 16
    rng = np.random.default_rng(123)
    probs = np.clip(float(row["pred_prob"]) + rng.normal(0, instability, size=runs), 0, 1)
    labels = (probs >= 0.5).astype(int)
    stable_rate = float(np.mean(labels == labels[0]))
    reliability_df = pd.DataFrame({"Run": np.arange(1, runs + 1), "Probability": probs})
    fig_rel = px.line(reliability_df, x="Run", y="Probability", markers=True)
    fig_rel.add_hline(y=0.5, line_dash="dash", line_color="#64748b")
    fig_rel.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font=dict(color="#334155"),
        margin=dict(l=10, r=10, t=20, b=10),
        yaxis=dict(range=[0, 1], gridcolor="#e2e8f0"),
    )
    st.plotly_chart(fig_rel, use_container_width=True)
    st.info(f"Stability rate in this demo: {stable_rate:.2f}. The closer this stays to 1.00, the easier the system is to trust operationally.")

with tabs[1]:
    st.markdown("**Safe means uncertain or unusual cases are slowed down before they can cause harm.**")
    safe_low_conf = float(row["confidence"]) < safe_s.conf_threshold
    safe_out_ctx = float(row["ood_score"]) > safe_s.ood_threshold
    fig_safe = go.Figure()
    fig_safe.add_shape(type="rect", x0=0, y0=safe_s.conf_threshold, x1=safe_s.ood_threshold, y1=1, fillcolor="rgba(34,197,94,0.08)", line_width=0)
    fig_safe.add_shape(type="rect", x0=safe_s.ood_threshold, y0=0, x1=1, y1=safe_s.conf_threshold, fillcolor="rgba(239,68,68,0.10)", line_width=0)
    fig_safe.add_vline(x=safe_s.ood_threshold, line_dash="dash", line_color="#f59e0b")
    fig_safe.add_hline(y=safe_s.conf_threshold, line_dash="dash", line_color="#f59e0b")
    fig_safe.add_trace(
        go.Scatter(
            x=[float(row["ood_score"])],
            y=[float(row["confidence"])],
            mode="markers+text",
            marker=dict(size=18, color="#ef4444" if (safe_low_conf or safe_out_ctx) else "#16a34a", symbol="star"),
            text=[row["case_id"]],
            textposition="top center",
            name="Selected case",
        )
    )
    fig_safe.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font=dict(color="#334155"),
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(title="Out-of-context score", range=[0, 1], gridcolor="#e2e8f0"),
        yaxis=dict(title="Confidence", range=[0, 1], gridcolor="#e2e8f0"),
    )
    st.plotly_chart(fig_safe, use_container_width=True)
    st.info("If the point sits in the riskier area, the safe response is to pause, review, or investigate rather than automate.")

with tabs[2]:
    st.markdown("**Fair means checking whether outcomes differ across groups and investigating gaps.**")
    fairness_rates = df_f.groupby("sensitive_group")["pred_label"].mean().reset_index(name="positive_rate")
    fairness_gap = float(fairness_rates["positive_rate"].max() - fairness_rates["positive_rate"].min()) if len(fairness_rates) > 1 else 0.0
    fig_fair = px.bar(
        fairness_rates,
        x="sensitive_group",
        y="positive_rate",
        color="sensitive_group",
        text=fairness_rates["positive_rate"].apply(lambda v: f"{v:.0%}"),
        color_discrete_sequence=["#3b82f6", "#a855f7"],
    )
    fig_fair.update_traces(textposition="outside")
    fig_fair.update_layout(
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="rgba(255,255,255,0)",
        font=dict(color="#334155"),
        margin=dict(l=10, r=10, t=20, b=10),
        showlegend=False,
        yaxis=dict(range=[0, 1.2], gridcolor="#e2e8f0", title="Positive rate"),
        xaxis=dict(title=""),
    )
    st.plotly_chart(fig_fair, use_container_width=True)
    st.info(f"Current demo fairness gap: {fairness_gap:.2f}. A gap is a prompt to investigate, not proof by itself.")

with tabs[3]:
    st.markdown("**Transparent means people can understand the main reasons behind an output.**")
    st.markdown(
        "".join(f'<div class="demo-reason">{reason}</div>' for reason in reasons),
        unsafe_allow_html=True,
    )
    st.markdown(
        (
            '<div class="demo-note">'
            "<strong>Ask next:</strong> what information, review, or changed context would alter this result?"
            "</div>"
        ),
        unsafe_allow_html=True,
    )

with tabs[4]:
    st.markdown("**Accountable means someone owns the decision, the review process, and the audit trail.**")
    audit = pd.DataFrame(
        [
            ("Decision owner", "Case officer / manager"),
            ("Human review active", "Yes" if safe_s.human_review_low_conf else "No"),
            ("Data-quality checks", "Yes" if safe_s.data_quality_checks else "No"),
            ("Confidence threshold", f"{safe_s.conf_threshold:.2f}"),
            ("OOD threshold", f"{safe_s.ood_threshold:.2f}"),
        ],
        columns=["Control", "Current demo state"],
    )
    st.dataframe(audit, use_container_width=True, hide_index=True)
    st.info("Accountability is not a model property. It is a governance choice about ownership, review, logging, and monitoring.")

st.divider()
st.caption("This demo uses simulated outputs and simplified indicators to make the governance logic easier to understand.")
