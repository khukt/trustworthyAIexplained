import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from trust_utils import apply_dark_theme

apply_dark_theme()

st.title("1\ufe0f\u20e3 What is Trustworthy AI?")
st.markdown(
    "<p style='color:#64748b; font-size:1.05rem;'>"
    "Trustworthy AI is AI that is <strong>reliable</strong>, <strong>safe</strong>, "
    "<strong>fair</strong>, <strong>transparent</strong>, and <strong>accountable</strong> — "
    "designed to earn and maintain human trust across real-world applications."
    "</p>",
    unsafe_allow_html=True,
)

st.divider()

# \u2500\u2500 Five pillars as styled cards \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
items = [
    ("\u2705", "Reliable", "#22c55e", "Stable performance, not random behavior."),
    ("\U0001f9ef", "Safe", "#ef4444", "Fail-safe rules and guardrails reduce harm."),
    ("\u2696\ufe0f", "Fair", "#f59e0b", "Checks reduce discriminatory outcomes."),
    ("\U0001f50e", "Transparent", "#3b82f6", "Decision reasoning is explainable and reviewable."),
    ("\U0001f9fe", "Accountable", "#a855f7", "Logs, audits, and ownership are defined."),
]
cols = st.columns(5)
for col, (icon, label, color, desc) in zip(cols, items):
    with col:
        st.markdown(
            f"""
            <div style='background:#f8fafc; border:1px solid {color};
                        border-top: 4px solid {color}; border-radius:12px;
                        padding:20px 14px; text-align:center; height:160px;
                        display:flex; flex-direction:column; justify-content:center;'>
              <div style='font-size:2rem;'>{icon}</div>
              <div style='color:{color}; font-weight:700; font-size:1.05rem;
                          margin:6px 0 4px;'>{label}</div>
              <div style='color:#475569; font-size:0.85rem;'>{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# \u2500\u2500 Radar chart + maturity bars \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
left, right = st.columns([1.1, 1], gap="large")

with left:
    pillar_labels = ["Reliable", "Safe", "Fair", "Transparent", "Accountable"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[0.90, 0.85, 0.80, 0.88, 0.82, 0.90],
        theta=pillar_labels + [pillar_labels[0]],
        fill="toself",
        name="With safeguards",
        line_color="#22c55e",
        fillcolor="rgba(34,197,94,0.20)",
    ))
    fig.add_trace(go.Scatterpolar(
        r=[0.45, 0.30, 0.35, 0.40, 0.28, 0.45],
        theta=pillar_labels + [pillar_labels[0]],
        fill="toself",
        name="Without safeguards",
        line_color="#ef4444",
        fillcolor="rgba(239,68,68,0.15)",
    ))
    fig.update_layout(
        polar=dict(
            bgcolor="#f8fafc",
            radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(color="#475569")),
            angularaxis=dict(tickfont=dict(color="#334155")),
        ),
        paper_bgcolor="#ffffff",
        legend=dict(font=dict(color="#334155"), bgcolor="#ffffff"),
        margin=dict(l=30, r=30, t=50, b=30),
        title=dict(text="Impact of Trustworthy AI practices", font=dict(color="#1e40af")),
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### What Trustworthy AI is *not*")
    for txt, icon in [
        ("A 'luxury feature'", "❌"),
        ("Only about accuracy", "❌"),
        ("About replacing people", "❌"),
    ]:
        st.markdown(
            f"<div style='background:#f8fafc; border:1px solid #e2e8f0; "
            f"border-radius:8px; padding:10px 14px; margin:6px 0; color:#dc2626;'>"
            f"{icon} {txt}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("### ✅ What it is")
    st.markdown(
        "<div style='background:#eff6ff; border:1px solid #2563eb; "
        "border-radius:8px; padding:14px 18px; color:#1e40af; font-size:1rem;'>"
        "🛡️ <strong>Risk management</strong> for AI-assisted decisions."
        "</div>",
        unsafe_allow_html=True,
    )

    # Maturity bar chart
    st.markdown("### Typical maturity without safeguards")
    df_mat = pd.DataFrame({
        "Pillar": pillar_labels,
        "Score (%)": [45, 30, 35, 40, 28],
    })
    fig2 = px.bar(
        df_mat, x="Score (%)", y="Pillar", orientation="h",
        color="Score (%)",
        color_continuous_scale=["#ef4444", "#f59e0b", "#22c55e"],
        range_color=[0, 100],
        text="Score (%)",
    )
    fig2.update_traces(texttemplate="%{text}%", textposition="inside")
    fig2.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#334155"),
        coloraxis_showscale=False,
        xaxis=dict(range=[0, 100], title="", showgrid=False),
        yaxis=dict(title=""),
        margin=dict(l=0, r=10, t=10, b=10),
        height=220,
    )
    st.plotly_chart(fig2, use_container_width=True)
