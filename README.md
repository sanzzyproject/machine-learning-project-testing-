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

---

### Cara Menjalankan Proyek Ini (Langkah Anda Sekarang)

1.  **Buat folder** dan file-file di atas di komputer Anda.
2.  **Download Dataset** (Misal: [Bank Customer Churn Prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)) dan simpan sebagai `churn.csv` di folder proyek.
3.  Buka terminal/CMD di folder tersebut.
4.  Jalankan training:
    `python src/train.py`
    *(Ini akan membuat file `models/churn_model.joblib`)*.
5.  Jalankan API:
    `uvicorn api.main:app --reload`
6.  Tes di browser: Buka `http://127.0.0.1:8000/docs`.

### Cara Upload ke GitHub

1.  Buka terminal di folder proyek.
2.  `git init`
3.  `git add .`
4.  `git commit -m "Initial commit: ChurnGuard full project structure"`
5.  Buat repository baru di GitHub (kosongkan saja).
6.  Ikuti instruksi GitHub untuk push (biasanya: `git remote add origin ...` lalu `git push -u origin master`).

## 🏗️ Project Architecture
The project follows a modular structure for maintainability:

```text
├── api/                # API Endpoints (FastAPI)
├── models/             # Serialized Models (Joblib)
├── src/                # Training Pipeline & Preprocessing
├── Dockerfile          # Container Configuration
└── requirements.txt    # Dependencies
