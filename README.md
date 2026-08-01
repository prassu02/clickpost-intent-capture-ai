# 📦 ClickPost Intent Capture AI Platform

> AI-powered Buying Intent Detection Platform that identifies high-intent companies from public signals, ranks leads, and automatically generates personalized outreach using LLMs.

---

## 🚀 Live Demo

### 🌐 Streamlit Dashboard
https://clickpost-intent-capture-ai-av4xntjk4qzp6bqmhvjpdf.streamlit.app/

### ⚡ FastAPI Backend
https://clickpost-intent-capture-ai-backend-api.onrender.com

### 📄 API Docs
https://clickpost-intent-capture-ai-backend-api.onrender.com/docs

---

# 📸 Screenshots

## Dashboard

<img width="1242" height="517" alt="dashboard" src="https://github.com/user-attachments/assets/8f402e4a-b4d6-44d4-bc6e-11c920bc9c86" />

---

## Company Ranking

<img width="1180" height="687" alt="company_ranking" src="https://github.com/user-attachments/assets/f9868f49-da95-4807-8c02-847341a91ef0" />

---

## Intent Signals

<img width="1225" height="680" alt="News_signals" src="https://github.com/user-attachments/assets/56a55ab9-0716-4b19-9891-6e1418caad04" />

---
## Graphs

<img width="1877" height="887" alt="Graphs" src="https://github.com/user-attachments/assets/900d9fe9-ac19-439c-9edd-d485c252fdfb" />

---

## AI Personalized Outreach

<img width="1807" height="790" alt="outreach" src="https://github.com/user-attachments/assets/deac13c4-f86d-4ed9-bc73-b96f7c1e119f" />

---
## AI Personalized Outreach Example Response
 
 <img width="1752" height="810" alt="Ai-outreach-reponse-example" src="https://github.com/user-attachments/assets/5a3ae21b-b45b-4d07-8dfe-b3cf2c85c9b9" />

---

# 🎯 Problem Statement

Sales teams spend countless hours identifying companies that may be ready to purchase logistics and shipping solutions.

This platform automates that process by:

- Collecting public buying intent signals
- Ranking companies based on intent
- Explaining why companies were scored
- Generating AI-powered personalized outreach

---

# ✨ Features

✅ Public signal collection

✅ Buying intent detection

✅ Explainable AI scoring

✅ Company ranking

✅ Personalized AI email generation

✅ Personalized LinkedIn generation

✅ FastAPI REST API

✅ Interactive Streamlit Dashboard

✅ Docker Deployment

---

# 🏗 System Architecture

```text
                  Public Sources
             (News / RSS Feeds)

                      │
                      ▼

         Signal Collection Pipeline
        (feedparser + requests)

                      │
                      ▼

           Intent Signal Extraction

                      │
                      ▼

            Company Score Engine

                      │
                      ▼

      AI Outreach Generator (Groq LLM)

          ┌──────────────┴──────────────┐
          ▼                             ▼

 Company Ranking CSV          Outreach CSV

          │
          ▼

     FastAPI Backend

          │
          ▼

  Streamlit Dashboard
```

---

# 🧠 AI Workflow

```text
Company List
      │
      ▼

Collect Public Signals
      │
      ▼

Intent Detection
      │
      ▼

Score Companies
      │
      ▼

Rank Companies
      │
      ▼

Generate AI Email
      │
      ▼

Generate LinkedIn Message
      │
      ▼

Dashboard + REST API
```

---

# 📂 Project Structure

```text
clickpost-intent-capture-ai/
│
├── api/
│   ├── __init__.py
│   └── app.py                     # FastAPI Backend
│
├── dashboard/
│   ├── __init__.py
│   └── app.py                     # Streamlit Dashboard
│
├── scraper/
│   ├── __init__.py
│   └── signal_collector.py        # RSS / News Signal Collection
│
├── scoring/
│   ├── __init__.py
│   └── score_engine.py            # Company Scoring Logic
│
├── generator/
│   ├── __init__.py
│   ├── llm_generator.py           # AI Email Generator
│   ├── outreach_generator.py      # LinkedIn Generator
│   └── save_outreach.py
│
├── signals/
│   ├── __init__.py
│   └── intent_rules.py            # Buying Intent Taxonomy
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── data/
│   │
│   ├── raw/
│   │   ├── companies.csv
│   │   └── sample_accounts.csv
│   │
│   └── output/
│       ├── company_ranking.csv
│       ├── news_signals.csv
│       └── personalized_outreach.csv
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .dockerignore
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── config.py
├── main.py                                                   # Run Complete AI Pipeline
├── ClickPost_Intent_Capture_AI_Project_Memo.pdf                     
├── requirements.txt
├── README.md
```

---

# ⚙ Tech Stack

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit

### AI

- Groq LLM

### Data

- Pandas
- NumPy

### Data Sources

- RSS Feeds
- News Sources

### Deployment

- Docker
- Render
- Streamlit Cloud

---

# 📊 Output Files

Generated automatically

```
company_ranking.csv

news_signals.csv

personalized_outreach.csv
```

---

# REST API

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

---

## Intent Signals

```
GET /signals
```

---

## AI Outreach

```
GET /outreach
```

---

# 🚀 Installation

Clone repository

```bash
git clone https://github.com/prassu02/clickpost-intent-capture-ai.git

cd clickpost-intent-capture-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create environment

```env
GROQ_API_KEY=YOUR_KEY
```

Run Pipeline

```bash
python main.py
```

Run FastAPI

```bash
uvicorn api.app:app --reload
```

Run Streamlit

```bash
streamlit run dashboard/app.py
```

---

# 🐳 Docker

Build

```bash
docker build -t clickpost-ai .
```

Run

```bash
docker run -p 8000:8000 clickpost-ai
```

---

# 📈 Future Improvements

- Reddit integration
- LinkedIn signal extraction
- Twitter/X integration
- Real-time scheduling
- PostgreSQL database
- Authentication
- Vector database
- Multi-agent workflow
- LangGraph integration

---

# 👨‍💻 Author

**Prasanna Kumar**

AI Engineer | Machine Learning Engineer | Data Scientist

GitHub

https://github.com/prassu02

LinkedIn

https://www.linkedin.com/in/k-prasanna-kumar/

---

⭐ If you found this project useful, consider giving it a star.
