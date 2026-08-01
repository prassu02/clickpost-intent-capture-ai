import pandas as pd
from pathlib import Path

from config import RAW_DATA_DIR, OUTPUT_DIR

from utils.helpers import (
    load_companies,
    save_signals
)

from scraper.signal_collector import (
    collect_signals
)

from scoring.score_engine import (
    rank_companies
)

from generator.outreach_generator import (
    generate_linkedin
)

from generator.llm_generator import (
    generate_ai_email
)

from generator.save_outreach import (
    save_outreach
)


# ==========================================================
# Create Output Directory
# ==========================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


print("=" * 70)
print("🚀 ClickPost Intent Capture AI Pipeline Started")
print("=" * 70)


# ==========================================================
# Load Companies
# ==========================================================

company_file = RAW_DATA_DIR / "sample_accounts.csv"


if not company_file.exists():

    raise FileNotFoundError(
        f"Company file missing: {company_file}"
    )


companies = load_companies(
    company_file
)


print(
    f"✅ Loaded Companies: {len(companies)}"
)


# ==========================================================
# Collect Intent Signals
# ==========================================================

all_signals = []


print("\n")
print("=" * 70)
print("🔎 Collecting Intent Signals")
print("=" * 70)


for company in companies["brand"]:

    print(
        f"Collecting signals for: {company}"
    )

    try:

        signals = collect_signals(company)

        if signals:

            all_signals.extend(signals)

    except Exception as e:

        print(
            f"❌ Error collecting {company}: {e}"
        )


print(
    f"\nTotal Signals Collected: {len(all_signals)}"
)



# ==========================================================
# Save Signals CSV
# ==========================================================

signals_path = OUTPUT_DIR / "news_signals.csv"


save_signals(
    all_signals,
    signals_path
)


print(
    f"✅ Signals Saved: {signals_path}"
)



# ==========================================================
# Convert Signals DataFrame
# ==========================================================

signals_df = pd.DataFrame(
    all_signals
)


if signals_df.empty:

    print(
        "⚠️ No signals found. Creating empty ranking."
    )

    ranking = pd.DataFrame(
        columns=[
            "company",
            "total_score",
            "priority",
            "reasons"
        ]
    )


else:

    # ======================================================
    # Company Ranking
    # ======================================================

    print("\n")
    print("=" * 70)
    print("🏆 Ranking Companies")
    print("=" * 70)


    ranking = rank_companies(
        signals_df
    )



# ==========================================================
# Save Ranking
# ==========================================================

ranking_path = OUTPUT_DIR / "company_ranking.csv"


ranking.to_csv(
    ranking_path,
    index=False
)


print(
    f"✅ Ranking Saved: {ranking_path}"
)


print("\nTop Companies")

print(
    ranking.head(10)
)



# ==========================================================
# Generate AI Outreach
# ==========================================================

print("\n")
print("=" * 70)
print("🤖 Generating AI Personalized Outreach")
print("=" * 70)


outreach_data = []


if not ranking.empty:


    for _, row in ranking.head(5).iterrows():


        company = row.get(
            "company",
            ""
        )


        reasons = row.get(
            "reasons",
            ""
        )


        print(
            f"\nGenerating outreach for {company}"
        )


        try:


            email = generate_ai_email(
                company,
                reasons
            )


            linkedin = generate_linkedin(
                company,
                reasons
            )


            outreach_data.append(
                {
                    "company": company,
                    "reasons": reasons,
                    "email": email,
                    "linkedin": linkedin
                }
            )


        except Exception as e:


            print(
                f"❌ Outreach failed for {company}: {e}"
            )



# ==========================================================
# Save Outreach
# ==========================================================

outreach_path = OUTPUT_DIR / "personalized_outreach.csv"


save_outreach(
    outreach_data,
    outreach_path
)


print(
    f"✅ Outreach Saved: {outreach_path}"
)



# ==========================================================
# Final Verification
# ==========================================================

print("\n")
print("=" * 70)
print("📁 Generated Files")
print("=" * 70)


for file in [
    signals_path,
    ranking_path,
    outreach_path
]:

    print(
        file,
        " -> ",
        file.exists(),
        " -> ",
        file.stat().st_size if file.exists() else 0,
        "bytes"
    )



print("\n")
print("=" * 70)
print("🎉 ClickPost Intent Capture AI Completed Successfully!")
print("=" * 70)
