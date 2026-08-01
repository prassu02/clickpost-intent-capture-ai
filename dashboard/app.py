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

# ==========================================================
# Backend URL
# ==========================================================
API_URL = "https://clickpost-intent-capture-ai-backend1.onrender.com"

# ==========================================================
# Helper Function
# ==========================================================
def load_api(endpoint):

    try:

        response = requests.get(
            f"{API_URL}/{endpoint}",
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        if isinstance(data, list):
            return pd.DataFrame(data)

        st.error(f"{endpoint} returned unexpected data.")
        st.write(data)

        return pd.DataFrame()

    except Exception as e:

        st.error(f"Failed to load '{endpoint}'")
        st.error(str(e))

        return pd.DataFrame()


# ==========================================================
# Load Data
# ==========================================================
ranking = load_api("ranking")
signals = load_api("signals")
outreach = load_api("outreach")

ranking = ranking.fillna("")
signals = signals.fillna("")
outreach = outreach.fillna("")

# ==========================================================
# Validate Ranking Data
# ==========================================================
if ranking.empty:

    st.warning("No Company Ranking data found.")

    st.write("Ranking DataFrame")
    st.write(ranking)

    st.stop()

required_columns = [
    "company",
    "total_score",
]

missing = [
    c
    for c in required_columns
    if c not in ranking.columns
]

if missing:

    st.error("Backend returned incorrect columns.")

    st.write("Missing Columns")
    st.write(missing)

    st.write("Received Columns")
    st.write(ranking.columns.tolist())

    st.write("Received Data")
    st.write(ranking)

    st.stop()

# ==========================================================
# Sidebar
# ==========================================================
st.sidebar.title("Dashboard Filters")

company_list = ["All"] + sorted(
    ranking["company"].astype(str).unique().tolist()
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

if (
    not signals.empty
    and "company" in signals.columns
):

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

if (
    not outreach.empty
    and "company" in outreach.columns
):

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
# Dashboard Summary
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

avg_score = round(
    ranking["total_score"].mean(),
    2,
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
    use_container_width=True,
)

st.download_button(
    "⬇ Download Company Ranking",
    filtered_ranking.to_csv(index=False),
    "company_ranking.csv",
    "text/csv",
)

st.divider()

# ==========================================================
# Intent Signals
# ==========================================================
st.subheader("📰 Intent Signals")

if filtered_signals.empty:

    st.info("No signal data available.")

else:

    st.dataframe(
        filtered_signals,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Signals",
        filtered_signals.to_csv(index=False),
        "news_signals.csv",
        "text/csv",
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

st.divider()

# ==========================================================
# Priority Distribution
# ==========================================================
if "priority" in ranking.columns:

    st.subheader("🔥 Lead Priority")

    st.bar_chart(
        ranking["priority"].value_counts()
    )

st.divider()

# ==========================================================
# Intent Distribution
# ==========================================================
if (
    not signals.empty
    and "intent" in signals.columns
):

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
# Outreach
# ==========================================================
st.subheader("🤖 AI Personalized Outreach")

if filtered_outreach.empty:

    st.info("No outreach available.")

else:

    for _, row in filtered_outreach.iterrows():

        with st.expander(f"📧 {row['company']}"):

            st.write("### Email")

            st.text_area(
                "Email",
                row["email"],
                height=220,
                key=f"email_{row['company']}",
            )

            st.write("### LinkedIn")

            st.text_area(
                "LinkedIn",
                row["linkedin"],
                height=120,
                key=f"linkedin_{row['company']}",
            )

    st.download_button(
        "⬇ Download Outreach",
        filtered_outreach.to_csv(index=False),
        "personalized_outreach.csv",
        "text/csv",
    )

st.divider()

st.success("✅ Dashboard Loaded Successfully")

st.caption(
    "Built using Python • FastAPI • Streamlit • Pandas • Matplotlib • Groq LLM"
)
