import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.title("1\ufe0f\u20e3 What is Trustworthy AI?")
st.markdown(
    "<p style='color:#94a3b8; font-size:1.05rem;'>"
    "Trustworthy AI is AI that is <strong>reliable</strong>, <strong>safe</strong>, "
    "<strong>fair</strong>, <strong>transparent</strong>, and <strong>accountable</strong> \u2014 "
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
            <div style='background:#1e293b; border:1px solid {color};
                        border-top: 4px solid {color}; border-radius:12px;
                        padding:20px 14px; text-align:center; height:160px;
                        display:flex; flex-direction:column; justify-content:center;'>
              <div style='font-size:2rem;'>{icon}</div>
              <div style='color:{color}; font-weight:700; font-size:1.05rem;
                          margin:6px 0 4px;'>{label}</div>
              <div style='color:#94a3b8; font-size:0.85rem;'>{desc}</div>
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
            bgcolor="#0f172a",
            radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(color="#64748b")),
            angularaxis=dict(tickfont=dict(color="#cbd5e1")),
        ),
        paper_bgcolor="#1e293b",
        legend=dict(font=dict(color="#cbd5e1"), bgcolor="#1e293b"),
        margin=dict(l=30, r=30, t=50, b=30),
        title=dict(text="Impact of Trustworthy AI practices", font=dict(color="#93c5fd")),
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### What Trustworthy AI is *not*")
    for txt, icon in [
        ("A 'luxury feature'", "\u274c"),
        ("Only about accuracy", "\u274c"),
        ("About replacing people", "\u274c"),
    ]:
        st.markdown(
            f"<div style='background:#1e293b; border:1px solid #374151; "
            f"border-radius:8px; padding:10px 14px; margin:6px 0; color:#f87171;'>"
            f"{icon} {txt}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("### \u2705 What it is")
    st.markdown(
        "<div style='background:#1e3a5f; border:1px solid #2563eb; "
        "border-radius:8px; padding:14px 18px; color:#93c5fd; font-size:1rem;'>"
        "\U0001f6e1\ufe0f <strong>Risk management</strong> for AI-assisted decisions."
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
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font=dict(color="#cbd5e1"),
        coloraxis_showscale=False,
        xaxis=dict(range=[0, 100], title="", showgrid=False),
        yaxis=dict(title=""),
        margin=dict(l=0, r=10, t=10, b=10),
        height=220,
    )
    st.plotly_chart(fig2, use_container_width=True)
