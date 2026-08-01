import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st

# ==========================================================
# Fix Import Path
# ==========================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# ==========================================================
# Page Config
# ==========================================================
st.set_page_config(
    page_title="ClickPost Intent Capture Dashboard",
    page_icon="📦",
    layout="wide",
)

st.title("📦 ClickPost Intent Capture Dashboard")
st.markdown("### AI-Powered Buying Intent Detection Platform")

API_URL = "https://clickpost-intent-capture-ai.onrender.com"

# ==========================================================
# Load Data
# ==========================================================
try:

    ranking = pd.DataFrame(
        requests.get(f"{API_URL}/ranking").json()
    )

    signals = pd.DataFrame(
        requests.get(f"{API_URL}/signals").json()
    )

    outreach = pd.DataFrame(
        requests.get(f"{API_URL}/outreach").json()
    )

except Exception as e:

    st.error("❌ FastAPI server is not running.")
    st.error(str(e))
    st.stop()

# ==========================================================
# Clean Data
# ==========================================================
ranking = ranking.fillna("")
signals = signals.fillna("")
outreach = outreach.fillna("")

# ==========================================================
# Sidebar
# ==========================================================
st.sidebar.title("Dashboard Filters")

company_list = ["All"] + sorted(
    ranking["company"].unique().tolist()
)

selected_company = st.sidebar.selectbox(
    "Select Company",
    company_list,
)

search = st.sidebar.text_input(
    "Search Company"
)

# ==========================================================
# Filter Ranking
# ==========================================================
filtered_ranking = ranking.copy()

if selected_company != "All":

    filtered_ranking = filtered_ranking[
        filtered_ranking["company"] == selected_company
    ]

if search:

    filtered_ranking = filtered_ranking[
        filtered_ranking["company"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

# ==========================================================
# Filter Signals
# ==========================================================
filtered_signals = signals.copy()

if selected_company != "All":

    filtered_signals = filtered_signals[
        filtered_signals["company"] == selected_company
    ]

if search:

    filtered_signals = filtered_signals[
        filtered_signals["company"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

# ==========================================================
# Filter Outreach
# ==========================================================
filtered_outreach = outreach.copy()

if selected_company != "All":

    filtered_outreach = filtered_outreach[
        filtered_outreach["company"] == selected_company
    ]

if search:

    filtered_outreach = filtered_outreach[
        filtered_outreach["company"].str.contains(
            search,
            case=False,
            na=False,
        )
    ]

# ==========================================================
# Dashboard Metrics
# ==========================================================
st.subheader("📊 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Companies",
    len(ranking),
)

col2.metric(
    "Signals",
    len(signals),
)

avg_score = (
    round(ranking["total_score"].mean(), 2)
    if not ranking.empty
    else 0
)

col3.metric(
    "Average Score",
    avg_score,
)

col4.metric(
    "AI Outreach",
    len(outreach),
)

st.divider()

# ==========================================================
# Company Ranking
# ==========================================================
st.subheader("🏆 Company Ranking")

st.dataframe(
    filtered_ranking,
    width="stretch",
)

st.download_button(
    label="⬇ Download Company Ranking",
    data=filtered_ranking.to_csv(index=False),
    file_name="company_ranking.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# Intent Signals
# ==========================================================
st.subheader("📰 Intent Signals")

st.dataframe(
    filtered_signals,
    width="stretch",
)

st.download_button(
    label="⬇ Download Signals",
    data=filtered_signals.to_csv(index=False),
    file_name="news_signals.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# Company Score Chart
# ==========================================================
st.subheader("📈 Company Scores")

if not filtered_ranking.empty:

    chart = filtered_ranking.set_index(
        "company"
    )["total_score"]

    st.bar_chart(chart)

else:

    st.info("No data available.")

st.divider()

# ==========================================================
# Lead Priority Distribution
# ==========================================================
if "priority" in ranking.columns:

    st.subheader("🔥 Lead Priority Distribution")

    priority_counts = ranking["priority"].value_counts()

    st.bar_chart(priority_counts)

st.divider()

# ==========================================================
# Intent Distribution
# ==========================================================
if "intent" in signals.columns:

    st.subheader("🥧 Intent Distribution")

    intent_counts = (
        signals["intent"]
        .replace("", "General")
        .fillna("General")
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        intent_counts,
        labels=intent_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    ax.axis("equal")

    st.pyplot(fig)

st.divider()

# ==========================================================
# AI Outreach
# ==========================================================
st.subheader("🤖 AI Personalized Outreach")

if filtered_outreach.empty:

    st.info("No outreach messages available.")

else:

    for _, row in filtered_outreach.iterrows():

        with st.expander(f"📧 {row['company']}"):

            st.write("### AI Generated Email")

            st.text_area(
                label="Email",
                value=row["email"],
                height=260,
                key=f"email_{row['company']}",
                label_visibility="collapsed",
            )

            st.write("### LinkedIn Message")

            st.text_area(
                label="LinkedIn",
                value=row["linkedin"],
                height=120,
                key=f"linkedin_{row['company']}",
                label_visibility="collapsed",
            )

st.download_button(
    label="⬇ Download Outreach CSV",
    data=filtered_outreach.to_csv(index=False),
    file_name="personalized_outreach.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# Footer
# ==========================================================
st.success("✅ Dashboard Loaded Successfully")

st.caption(
    "Built using Python • FastAPI • Streamlit • Pandas • Matplotlib • Groq LLM"
)
