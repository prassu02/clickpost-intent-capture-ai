import pandas as pd


def priority(score):
    """
    Assign priority based on total score.
    """

    if score >= 60:
        return "🔥 Hot"

    elif score >= 40:
        return "🟡 Warm"

    else:
        return "❄️ Cold"


def get_reasons(intent_series):
    """
    Return clean, unique intent reasons.
    """

    cleaned = []

    for item in intent_series:

        if pd.isna(item):
            continue

        item = str(item).strip()

        if item.lower() == "general":
            continue

        cleaned.append(item)

    if not cleaned:
        return "General"

    return ", ".join(sorted(set(cleaned)))


def rank_companies(signals_df):
    """
    Rank companies based on collected signals.
    """

    # Ensure intent column exists
    if "intent" not in signals_df.columns:
        signals_df["intent"] = "General"

    # Replace missing values
    signals_df["intent"] = signals_df["intent"].fillna("General")

    grouped = (
        signals_df.groupby("company")
        .agg(
            total_score=("score", "sum"),
            signal_count=("score", "count"),
            reasons=("intent", get_reasons),
        )
        .reset_index()
    )

    # Sort by highest score
    grouped = grouped.sort_values(
        by="total_score",
        ascending=False,
    )

    # Add rank
    grouped["rank"] = range(1, len(grouped) + 1)

    # Add priority
    grouped["priority"] = grouped["total_score"].apply(priority)

    return grouped