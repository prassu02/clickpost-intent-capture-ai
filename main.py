import pandas as pd

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
# Load Companies
# ==========================================================

companies = load_companies(
    RAW_DATA_DIR / "sample_accounts.csv"
)

all_signals = []

print("=" * 60)
print("Collecting Intent Signals")
print("=" * 60)

# ==========================================================
# Collect Signals
# ==========================================================

for company in companies["brand"]:

    print(f"Collecting {company}")

    signals = collect_signals(company)

    all_signals.extend(signals)

# ==========================================================
# Save Signals
# ==========================================================

save_signals(
    all_signals,
    OUTPUT_DIR / "news_signals.csv"
)

signals_df = pd.DataFrame(all_signals)

# ==========================================================
# Rank Companies
# ==========================================================

ranking = rank_companies(signals_df)

ranking.to_csv(
    OUTPUT_DIR / "company_ranking.csv",
    index=False
)

print("\nTop Companies\n")

print(ranking.head(10))

# ==========================================================
# Generate Personalized Outreach
# ==========================================================

print("\n")
print("=" * 60)
print("Top 5 Personalized Outreach")
print("=" * 60)

outreach_data = []

for _, row in ranking.head(5).iterrows():

    company = row["company"]
    reasons = row["reasons"]

    print("\n")
    print("=" * 60)
    print(company)
    print("=" * 60)

    # Generate AI Email
    email = generate_ai_email(company, reasons)

    # Generate LinkedIn Message
    linkedin = generate_linkedin(company, reasons)

    # Save for CSV
    outreach_data.append(
        {
            "company": company,
            "reasons": reasons,
            "email": email,
            "linkedin": linkedin
        }
    )

    # Print Output
    print(email)
    print()
    print(linkedin)

# ==========================================================
# Save Outreach
# ==========================================================

save_outreach(
    outreach_data,
    OUTPUT_DIR / "personalized_outreach.csv"
)

print("\n")
print("=" * 60)
print("Files Saved Successfully")
print("=" * 60)

print(f"✓ News Signals      : {OUTPUT_DIR / 'news_signals.csv'}")
print(f"✓ Company Ranking   : {OUTPUT_DIR / 'company_ranking.csv'}")
print(f"✓ AI Outreach       : {OUTPUT_DIR / 'personalized_outreach.csv'}")

print("\nProject Completed Successfully! 🚀")