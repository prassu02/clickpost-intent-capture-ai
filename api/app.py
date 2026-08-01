from pathlib import Path
import os

import pandas as pd
from fastapi import FastAPI

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title="ClickPost Intent Capture API",
    version="2.0.0",
)

# ==========================================================
# Startup Debug
# ==========================================================

print("=" * 80)
print("Current Working Directory :", os.getcwd())
print("BASE_DIR                  :", BASE_DIR)
print("OUTPUT_DIR                :", OUTPUT_DIR)
print("OUTPUT EXISTS             :", OUTPUT_DIR.exists())

if OUTPUT_DIR.exists():

    print("\nFiles:")

    files = list(OUTPUT_DIR.glob("*"))

    if files:

        for f in files:
            print(f" - {f.name} ({f.stat().st_size} bytes)")

    else:

        print("No CSV files found.")

print("=" * 80)


# ==========================================================
# Helper
# ==========================================================

def load_csv(filename: str):

    file = OUTPUT_DIR / filename

    print("\n" + "=" * 80)
    print("Loading:", file)

    if not file.exists():

        print("File NOT Found")

        return {
            "success": False,
            "error": f"{filename} not found",
            "path": str(file),
        }

    try:

        df = pd.read_csv(file)

        df = df.fillna("")

        print("Rows:", len(df))
        print("Columns:", list(df.columns))

        return df.to_dict(orient="records")

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "path": str(file),
        }


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
            {
                "name": f.name,
                "size": f.stat().st_size,
            }
            for f in OUTPUT_DIR.glob("*")
        ],
    }


# ==========================================================
# Ranking
# ==========================================================

@app.get("/ranking")
def ranking():

    return load_csv("company_ranking.csv")


# ==========================================================
# Signals
# ==========================================================

@app.get("/signals")
def signals():

    return load_csv("news_signals.csv")


# ==========================================================
# Outreach
# ==========================================================

@app.get("/outreach")
def outreach():

    return load_csv("personalized_outreach.csv")
