# 📦 ClickPost Intent Capture AI Platform

> AI-powered buying intent detection platform for identifying high-potential eCommerce brands and generating personalized sales outreach.

---

# 🚀 Overview

The ClickPost Intent Capture AI Platform automatically discovers buying intent signals from multiple online sources, ranks companies based on their likelihood to purchase logistics software, and generates personalized AI-powered outreach emails and LinkedIn messages.

This project demonstrates an end-to-end AI workflow combining web scraping, NLP-based intent detection, scoring, ranking, FastAPI, Streamlit, and Large Language Models (LLMs).

---

# 🎯 Objectives

- Collect buying intent signals from public sources
- Identify companies showing growth or operational changes
- Rank companies using a weighted scoring engine
- Generate personalized outreach messages using AI
- Visualize results in an interactive dashboard
- Provide REST APIs for frontend integration

---

# ✨ Features

## Intent Signal Collection

- Google News RSS
- Hiring Activity
- Reddit Mentions (Demo)
- Company Growth Signals

---

## AI Intent Classification

Automatically detects signals such as:

- Hiring
- Expansion
- Funding
- Leadership Changes
- Product Launches
- Partnerships
- General News

---

## Company Ranking

Each company receives:

- Intent Score
- Signal Count
- Primary Reason
- Priority Level

Example:

| Company | Score | Priority |
|---------|-------|----------|
| Caraway | 65 | 🔥 Hot |
| Chubbies | 45 | 🟡 Warm |
| True Classic | 45 | 🟡 Warm |

---

## AI Personalized Outreach

Automatically generates:

- Sales Email
- LinkedIn Message

using

- Groq LLM
- Llama Models

---

## REST API

FastAPI endpoints:

```
GET /
GET /ranking
GET /signals
GET /outreach
```

---

## Dashboard

Interactive Streamlit dashboard including:

- KPI Metrics
- Company Rankings
- Intent Signals
- Priority Distribution
- Company Score Charts
- AI Outreach Viewer
- CSV Downloads

---

# 🛠 Tech Stack

### Backend

- Python 3.11
- FastAPI
- Uvicorn

### Dashboard

- Streamlit
- Matplotlib
- Pandas

### AI

- Groq API
- Llama Models

### Data Collection

- Google News RSS
- Feedparser
- Requests

---

# 📂 Project Structure

```
clickpost-intent-capture-ai/
│
├── api/
│   ├── __init__.py
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── scraper/
│   ├── jobs_scraper.py
│   ├── news_scraper.py
│   ├── reddit_scraper.py
│   └── signal_collector.py
│
├── scoring/
│   └── score_engine.py
│
├── generator/
│   ├── llm_generator.py
│   └── outreach_generator.py
│
├── utils/
│
├── data/
│   ├── raw/
│   └── output/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/clickpost-intent-capture-ai.git

cd clickpost-intent-capture-ai
```

Create virtual environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

Example

```text
GROQ_API_KEY=your_groq_api_key

OPENAI_API_KEY=

NEWS_API_KEY=

REDDIT_CLIENT_ID=

REDDIT_CLIENT_SECRET=

REDDIT_USER_AGENT=clickpost-intent-bot

MAX_RESULTS=10

TOP_ACCOUNTS=5
```

Only **GROQ_API_KEY** is required for the current implementation.

---

# ▶ Running the Project

## Step 1

Generate signals and rankings

```bash
python main.py
```

Output

```
news_signals.csv

company_ranking.csv

personalized_outreach.csv
```

---

## Step 2

Start FastAPI

```bash
uvicorn api.app:app --reload
```

API

```
http://127.0.0.1:8000
```

---

## Step 3

Launch Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard

```
http://localhost:8501
```

---

# 📊 Outputs

The project generates:

```
data/output/news_signals.csv

data/output/company_ranking.csv

data/output/personalized_outreach.csv
```

---

# 📡 API Endpoints

## Home

```
GET /
```

Returns API status.

---

## Company Ranking

```
GET /ranking
```

Returns ranked companies.

---

## Signals

```
GET /signals
```

Returns all collected intent signals.

---

## Outreach

```
GET /outreach
```

Returns AI-generated emails and LinkedIn messages.

---

# 📈 Workflow

```
Sample Accounts CSV
          │
          ▼
Signal Collection
          │
          ▼
Intent Classification
          │
          ▼
Company Scoring
          │
          ▼
Ranking Engine
          │
          ▼
AI Outreach Generation
          │
          ▼
CSV Export
          │
          ▼
FastAPI
          │
          ▼
Streamlit Dashboard
```

---

# 📷 Screenshots

Add screenshots of:

- Dashboard Home
- Company Rankings
- Intent Signals
- AI Outreach
- Charts

---

# 🔮 Future Improvements

- LinkedIn Scraper
- Reddit API Integration
- NewsAPI Integration
- Email Automation
- CRM Integration
- Lead Recommendation Engine
- Real-time Scheduler
- Docker Deployment
- Cloud Deployment
- Authentication

---

# 👨‍💻 Author

**Prasanna Kumar**

Artificial Intelligence & Data Science Engineer

Machine Learning | Generative AI | LLM | FastAPI | Streamlit

GitHub:
https://github.com/prassu02

LinkedIn:
https://www.linkedin.com/in/k-prasanna-kumar/

---

# 📄 License

This project is developed as part of the **ClickPost AI Intern Assignment** and is intended for educational and evaluation purposes.