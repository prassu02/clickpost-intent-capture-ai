from pathlib import Path
import os

import pandas as pd
from fastapi import FastAPI

# ==========================================================
# Paths
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "output"

print("=" * 70)
print("Current Working Directory :", os.getcwd())
print("BASE_DIR                  :", BASE_DIR)
print("OUTPUT_DIR                :", OUTPUT_DIR)
print("OUTPUT_DIR Exists         :", OUTPUT_DIR.exists())

if OUTPUT_DIR.exists():
    print("\nFiles in OUTPUT_DIR:")
    for f in OUTPUT_DIR.iterdir():
        print(f" - {f.name} ({f.stat().st_size} bytes)")
else:
    print("OUTPUT_DIR does not exist!")

print("=" * 70)

# ==========================================================
# FastAPI App
# ==========================================================
app = FastAPI(
    title="ClickPost Intent Capture API",
    version="2.0"
)


# ==========================================================
# Home
# ==========================================================
@app.get("/")
def home():

    return {
        "message": "ClickPost Intent Capture API Running",
        "base_dir": str(BASE_DIR),
        "output_dir": str(OUTPUT_DIR),
        "output_exists": OUTPUT_DIR.exists(),
        "files": [
            f.name for f in OUTPUT_DIR.glob("*")
        ] if OUTPUT_DIR.exists() else []
    }


# ==========================================================
# Company Ranking
# ==========================================================
@app.get("/ranking")
def ranking():

    file = OUTPUT_DIR / "company_ranking.csv"

    print("\n" + "=" * 70)
    print("Reading:", file)
    print("Exists :", file.exists())

    if not file.exists():
        return {
            "error": "company_ranking.csv not found",
            "path": str(file)
        }

    df = pd.read_csv(file)

    print("Rows    :", len(df))
    print("Columns :", list(df.columns))

    if len(df) > 0:
        print(df.head())

    return df.fillna("").to_dict(orient="records")


# ==========================================================
# Intent Signals
# ==========================================================
@app.get("/signals")
def signals():

    file = OUTPUT_DIR / "news_signals.csv"

    print("\n" + "=" * 70)
    print("Reading:", file)
    print("Exists :", file.exists())

    if not file.exists():
        return {
            "error": "news_signals.csv not found",
            "path": str(file)
        }

    df = pd.read_csv(file)

    print("Rows    :", len(df))
    print("Columns :", list(df.columns))

    if len(df) > 0:
        print(df.head())

    return df.fillna("").to_dict(orient="records")


# ==========================================================
# Personalized Outreach
# ==========================================================
@app.get("/outreach")
def outreach():

    file = OUTPUT_DIR / "personalized_outreach.csv"

    print("\n" + "=" * 70)
    print("Reading:", file)
    print("Exists :", file.exists())

    if not file.exists():
        return {
            "error": "personalized_outreach.csv not found",
            "path": str(file)
        }

    df = pd.read_csv(file)

    print("Rows    :", len(df))
    print("Columns :", list(df.columns))

    if len(df) > 0:
        print(df.head())

    return df.fillna("").to_dict(orient="records")
