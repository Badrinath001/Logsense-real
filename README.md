# LogSense Real - AI Log Intelligence Platform

Real-time AI-powered log analysis with FastAPI, Pydantic AI & Groq LLM.

![Docker](https://img.shields.io/badge/Docker-Ready-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Production-green) ![PydanticAI](https://img.shields.io/badge/Pydantic_AI-Agent-purple)

## 🚀 Live Demo
`docker run -p 8000:8000 -e GROQ_API_KEY=your_key badrinath001/logsense-real`

## 🧠 What it does
Ingests server logs → AI agent detects anomalies, root cause & severity → Structured JSON via Pydantic AI → Real-time dashboard

## 🏗️ Architecture

## ⚡ Tech Stack
- **Backend:** FastAPI, Pydantic, Pydantic AI
- **AI:** Groq (Llama 3.3 70B) - 10x faster than OpenAI
- **Infra:** Docker, SQLite, Uvicorn
- **Features:** Real-time streaming, Root cause analysis, Severity scoring

## 🔧 Run Locally
```bash
git clone https://github.com/Badrinath001/Logsense-real.git
cd Logsense-real
pip install -r requirements.txt
echo "GROQ_API_KEY=gsk_xxx" > .env
uvicorn app:app --reload
