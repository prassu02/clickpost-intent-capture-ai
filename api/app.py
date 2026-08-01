from pathlib import Path
import os
import sys
import subprocess

import pandas as pd
from fastapi import FastAPI

# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "data" / "output"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

REQUIRED_FILES = [
    OUTPUT_DIR / "company_ranking.csv",
    OUTPUT_DIR / "news_signals.csv",
    OUTPUT_DIR / "personalized_outreach.csv",
]

# ==========================================================
# Generate CSV Files if Missing
# ==========================================================

missing_files = [
    file.name
    for file in REQUIRED_FILES
    if not file.exists()
]

if missing_files:

    print("=" * 70)
    print("Missing output files:")
    print(missing_files)
    print("Running main.py...")
    print("=" * 70)

    try:

        subprocess.run(
            [sys.executable, "main.py"],
            cwd=BASE_DIR,
            check=True
        )

        print("main.py executed successfully.")

    except Exception as e:

        print("Failed to generate CSV files")
        print(e)

print("=" * 70)
print("Current Working Directory :", os.getcwd())
print("BASE_DIR                  :", BASE_DIR)
print("OUTPUT_DIR                :", OUTPUT_DIR)
print("OUTPUT_DIR Exists         :", OUTPUT_DIR.exists())

if OUTPUT_DIR.exists():

    print("\nFiles in OUTPUT_DIR")

    for file in OUTPUT_DIR.glob("*"):

        print(
            f"{file.name} ({file.stat().st_size} bytes)"
        )

print("=" * 70)

# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title="ClickPost Intent Capture API",
    version="2.0"
)

# ==========================================================
# Utility Function
# ==========================================================

def load_csv(filename: str):

    file = OUTPUT_DIR / filename

    if not file.exists():

        return {
            "error": f"{filename} not found",
            "path": str(file)
        }

    try:

        df = pd.read_csv(file)

        df = df.fillna("")

        return df.to_dict(orient="records")

    except Exception as e:

        return {
            "error": str(e),
            "path": str(file)
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
                "size": f.stat().st_size
            }
            for f in OUTPUT_DIR.glob("*")
        ]
    }

# ==========================================================
# Debug
# ==========================================================

@app.get("/debug")
def debug():

    return {
        "cwd": os.getcwd(),
        "base_dir": str(BASE_DIR),
        "output_dir": str(OUTPUT_DIR),
        "output_exists": OUTPUT_DIR.exists(),
        "files": [
            {
                "name": f.name,
                "size": f.stat().st_size
            }
            for f in OUTPUT_DIR.glob("*")
        ]
    }

# ==========================================================
# Company Ranking
# ==========================================================

@app.get("/ranking")
def ranking():

    return load_csv(
        "company_ranking.csv"
    )

# ==========================================================
# News Signals
# ==========================================================

@app.get("/signals")
def signals():

    return load_csv(
        "news_signals.csv"
    )

# ==========================================================
# Personalized Outreach
# ==========================================================

@app.get("/outreach")
def outreach():

    return load_csv(
        "personalized_outreach.csv"
    )
