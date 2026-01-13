# 🛡️ ChurnGuard: Intelligent Customer Retention System

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7-red?style=for-the-badge)

**ChurnGuard** is a production-grade Machine Learning solution designed to predict the likelihood of bank customer churn. It leverages **XGBoost** for high-accuracy classification and is served via a robust **FastAPI** interface, fully containerized with **Docker**.

## 💼 Business Context
Customer acquisition costs 5x more than retention. This tool allows Relationship Managers to:
1.  **Identify** high-risk customers instantly.
2.  **Understand** churn probability scores.
3.  **Act** proactively to retain valuable assets.

## 🏗️ Project Architecture
The project follows a modular structure for maintainability:

```text
├── api/                # API Endpoints (FastAPI)
├── models/             # Serialized Models (Joblib)
├── src/                # Training Pipeline & Preprocessing
├── Dockerfile          # Container Configuration
└── requirements.txt    # Dependencies

##INSTALLATION

git clone [https://github.com/YOUR_USERNAME/churn-guard.git](https://github.com/YOUR_USERNAME/churn-guard.git)
cd churn-guard
pip install -r requirements.txt

##Train the Model
This script processes the raw data, trains the XGBoost model, and saves the artifact to models/.

python src/train.py


##Run the API (Locally)
Launch the REST API server:

uvicorn api.main:app --reload


##Run with Docker 🐳
Build and run the containerized application:

docker build -t churn-guard .
docker run -p 8000:8000 churn-guard
