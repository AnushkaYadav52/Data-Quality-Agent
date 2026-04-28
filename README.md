# 🧹 AI Data Quality ELT Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![GROQ](https://img.shields.io/badge/GROQ-LLaMA%203-purple.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)

---

## 🚀 Overview

An end-to-end **data quality monitoring + AI explanation system** built using Python, Pandas, and GROQ LLMs.

It automatically detects data issues, explains them in natural language, and generates SQL-based fixes — all inside a modern Streamlit dashboard.

---

## 🧠 What This Project Does

This pipeline simulates a real-world **Data Engineering + AI Observability system**:

- 📥 Fetches data from an external API  
- 🐼 Runs automated data quality checks  
- 🚨 Detects issues (missing values, duplicates, invalid emails, empty strings)  
- 🤖 Sends issues to a GROQ LLM (LLaMA 3) for explanation + SQL fixes  
- 🧾 Generates structured JSON reports  
- 🎛️ Displays everything in a modern Streamlit dashboard  

---

## 🏗️ Architecture

API → Pandas DataFrame → Data Quality Checks → GROQ AI → JSON Report → Streamlit UI

---

## ✨ Features

### 🔍 Data Quality Engine
- Missing value detection  
- Duplicate row detection  
- Invalid email format detection  
- Empty string detection  

### 🤖 AI Layer (GROQ LLM)
- Converts raw issues into human-readable explanations  
- Provides SQL-based fixes for each issue  
- Structured, concise output format  

### 📊 Streamlit Dashboard
- Dark SaaS-style UI  
- Interactive dataset preview  
- Real-time issue detection  
- AI-generated insights  
- Downloadable JSON reports  

### 🧾 Reporting System
- Timestamped reports  
- JSON output for auditing / logging  
- Backend + frontend export support  

---

## 🛠️ Tech Stack

- Python 🐍  
- Pandas  
- Streamlit  
- Requests  
- GROQ API (LLaMA 3)  
- python-dotenv  

---

## 📂 Project Structure

ai/               → AI explanation logic (GROQ integration)
api/              → API data fetching + simulation
checks/           → Data validation rules
utils/            → Report generation system
data/             → Sample datasets
streamlit_app.py  → Dashboard UI
main.py           → CLI pipeline runner

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/your-username/data-quality-agent.git  
cd data-quality-agent  

---

### 2️⃣ Install dependencies

pip install -r requirements.txt  

---

### 3️⃣ Create environment variables

GROQ_API_KEY=your_api_key_here  

---

### 4️⃣ Run the application

streamlit run streamlit_app.py  

---

## 🔐 Security Notes

- `.env` file is excluded via `.gitignore`  
- API keys are never committed  
- Sensitive data stays local  

---

## 📈 Future Improvements

- Real-time streaming ingestion (Kafka / Airflow)  
- ML-based anomaly detection  
- Cloud deployment (AWS / GCP)  
- Monitoring dashboards (Prometheus / Grafana)  
- CI/CD pipeline with GitHub Actions  

---

## ⭐ If you like this project

Star the repo, fork it, or build on top of it 🚀
