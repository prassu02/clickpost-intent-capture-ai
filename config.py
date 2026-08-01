import os
from pathlib import Path

from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = DATA_DIR / "output"

# Create directories automatically
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# API Keys
# ==========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")

REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")

REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "")

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")

# ==========================================================
# Project Settings
# ==========================================================

MAX_RESULTS = int(os.getenv("MAX_RESULTS", 10))

TOP_ACCOUNTS = int(os.getenv("TOP_ACCOUNTS", 5))

# ==========================================================
# Debug Information
# ==========================================================

print("=" * 70)
print("BASE_DIR            :", BASE_DIR)
print("DATA_DIR            :", DATA_DIR)
print("RAW_DATA_DIR        :", RAW_DATA_DIR)
print("PROCESSED_DATA_DIR  :", PROCESSED_DATA_DIR)
print("OUTPUT_DIR          :", OUTPUT_DIR)
print("OUTPUT_DIR Exists   :", OUTPUT_DIR.exists())
print("=" * 70)
