# 🧹 AI Data Quality Agent

AI Data Quality Agent is a data engineering project that automatically detects data issues, explains them using an LLM, and generates structured reports. It combines Python, Pandas, and GROQ LLMs with a Streamlit dashboard for visualization.

## 🚀 Overview

An end-to-end data quality monitoring system built using Python, Pandas, and GROQ LLMs.

It detects data issues, explains them in natural language, and generates SQL-based fixes through an AI model, all inside a Streamlit dashboard.

## 🧠 What This Project Does

- 📥 Fetches data from an external API  
- 🐼 Runs automated data quality checks  
- 🚨 Detects issues such as missing values, duplicates, invalid emails, and empty strings  
- 🤖 Sends issues to a GROQ LLM (LLaMA 3) for explanation and SQL fixes  
- 🧾 Generates structured JSON reports  
- 🎛️ Displays everything in a Streamlit dashboard  

## 🏗️ Architecture

API → Pandas DataFrame → Data Quality Checks → GROQ AI → JSON Report → Streamlit UI

## ✨ Features

### 🔍 Data Quality Engine
- Missing value detection  
- Duplicate row detection  
- Invalid email format detection  
- Empty string detection  

### 🤖 AI Explanation Layer
- Converts raw issues into human-readable explanations  
- Provides SQL-based fixes  
- Structured and consistent output format  

### 📊 Streamlit Dashboard
- Dark SaaS-style interface  
- Dataset preview  
- Issue visualization  
- AI-generated explanations  
- JSON report download  

### 🧾 Reporting System
- Timestamped reports  
- JSON export format  
- Backend + frontend report generation  

## 🛠️ Tech Stack

- Python  
- Pandas  
- Streamlit  
- Requests  
- GROQ API (LLaMA 3)  
- python-dotenv  

## 📂 Project Structure

ai/ → AI explanation logic (GROQ integration)  
api/ → API data fetching and simulation  
checks/ → Data validation rules  
utils/ → Report generation system  
data/ → Sample datasets  
streamlit_app.py → Dashboard UI  
main.py → CLI pipeline runner  

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/AnushkaYadav52/Data-Quality-Agent
cd data-quality-agent  

### 2. Install dependencies

pip install -r requirements.txt  

### 3. Create environment variables

GROQ_API_KEY=your_api_key_here  

### 4. Run the application

streamlit run streamlit_app.py  

## 🔐 Security Notes

- `.env` file is ignored using `.gitignore`  
- API keys are never committed  
- Sensitive data stays local  

## 📈 Future Improvements

- Real-time streaming ingestion (Kafka / Airflow)  
- Machine learning-based anomaly detection  
- Cloud deployment (AWS / GCP / Azure)  
- Monitoring dashboards (Prometheus / Grafana)  
- CI/CD pipeline with GitHub Actions  
