from pathlib import Path

import pandas as pd
from fastapi import FastAPI

# ==========================================================
# Paths
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "data" / "output"

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
        "endpoints": [
            "/ranking",
            "/signals",
            "/outreach"
        ]
    }

# ==========================================================
# Company Ranking
# ==========================================================
@app.get("/ranking")
def ranking():

    file = OUTPUT_DIR / "company_ranking.csv"

    if not file.exists():

        return []

    df = pd.read_csv(file)

    df = df.fillna("")

    return df.to_dict(orient="records")

# ==========================================================
# Intent Signals
# ==========================================================
@app.get("/signals")
def signals():

    file = OUTPUT_DIR / "news_signals.csv"

    if not file.exists():

        return []

    df = pd.read_csv(file)

    df = df.fillna("")

    return df.to_dict(orient="records")

# ==========================================================
# Personalized Outreach
# ==========================================================
@app.get("/outreach")
def outreach():

    file = OUTPUT_DIR / "personalized_outreach.csv"

    if not file.exists():

        return []

    df = pd.read_csv(file)

    df = df.fillna("")

    return df.to_dict(orient="records")