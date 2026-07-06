# 📈 Retail Demand Forecasting using XGBoost, FastAPI, Streamlit & Docker

An end-to-end Machine Learning application that predicts future retail product demand using historical sales data. The project includes a complete ML pipeline, REST API, interactive dashboard, Docker containerization, and is designed for cloud deployment on AWS.

---

## 🚀 Project Overview

Retail businesses need accurate demand forecasting to optimize inventory, reduce stockouts, and minimize overstocking. This project builds a production-ready demand forecasting system using XGBoost and deploys it with FastAPI and Streamlit.

The application enables users to:

- Predict future sales demand
- Interact with a web dashboard
- Access predictions through REST APIs
- Visualize model performance
- Deploy using Docker
- Deploy on AWS (EC2) *(In Progress)*

---

# 🏗️ Project Architecture

```
                Historical Sales Data
                        │
                        ▼
                Data Preprocessing
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
              XGBoost Regression Model
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
     FastAPI API                 Streamlit Dashboard
         │                             │
         └──────────────┬──────────────┘
                        ▼
                   Docker Container
                        │
                        ▼
                 AWS Deployment
```

---

# 📂 Project Structure

```
retail-demand-forecasting
│
├── app
│   ├── api.py
│   └── dashboard.py
│
├── artifacts
│   ├── feature_importance.csv
│   ├── metrics.json
│   └── training.log
│
├── data
│   └── raw
│       ├── train.csv
│       └── test.csv
│
├── models
│   └── xgboost_model.pkl
│
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   └── 03_Training.ipynb
│
├── src
│   ├── data
│   ├── features
│   ├── models
│   └── utils
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

### Programming

- Python

### Machine Learning

- XGBoost
- Scikit-Learn
- Pandas
- NumPy

### API

- FastAPI
- Uvicorn

### Dashboard

- Streamlit

### Visualization

- Matplotlib
- Plotly

### DevOps

- Docker
- Git
- GitHub

### Cloud

- AWS EC2 *(Deployment In Progress)*
- AWS S3 *(Planned)*

---

# 📊 Feature Engineering

The following features are generated before model training:

- Store
- Item
- Year
- Month
- Day
- Day of Week
- Day of Year
- Week of Year
- Quarter
- Weekend Indicator
- Lag 1
- Lag 7
- Lag 30
- Rolling Mean (7)
- Rolling Mean (30)
- Rolling Std (7)

---

# 🤖 Machine Learning Model

Model Used:

- XGBoost Regressor

Evaluation Metrics:

| Metric | Score |
|---------|-------|
| MAE | 6.09 |
| RMSE | 7.92 |
| R² Score | 0.937 |

---

# 🌐 FastAPI Endpoints

## Health Check

```
GET /
```

## Predict

```
POST /predict
```

Swagger UI

```
http://localhost:8000/docs
```

---

# 📈 Streamlit Dashboard

The dashboard provides:

- Retail demand prediction
- Interactive user interface
- Feature importance visualization
- Prediction history
- Download prediction results
- Model information
- Dataset summary

Run locally:

```bash
streamlit run app/dashboard.py
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t retail-demand-forecasting .
```

Run Docker Container

```bash
docker run -p 8501:8501 retail-demand-forecasting
```

---

# ▶️ Running the Project

Clone repository

```bash
git clone https://github.com/mani7204mani/retail-demand-forecasting.git
```

Navigate

```bash
cd retail-demand-forecasting
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train model

```bash
python -m src.models.train
```

Run FastAPI

```bash
uvicorn app.api:app --reload
```

Run Streamlit

```bash
streamlit run app/dashboard.py
```

---

# 📌 Future Enhancements

- AWS EC2 Deployment
- Amazon S3 Model Storage
- CloudWatch Logging
- AWS Lambda Retraining
- CI/CD using GitHub Actions
- Docker Compose
- MLflow Experiment Tracking
- SHAP Explainability
- Batch Prediction using CSV Upload

---

# 📷 Project Screenshots

### Dashboard

_Add screenshot here_

### Swagger API

_Add screenshot here_

### Docker

_Add screenshot here_

---

# 📈 Results

✔ End-to-End ML Pipeline

✔ Feature Engineering

✔ XGBoost Regression

✔ FastAPI REST API

✔ Streamlit Dashboard

✔ Dockerized Application

✔ Modular Project Structure

✔ Production-Ready Architecture

---

# 👨‍💻 Author

**Mani Shankar Reddy**

GitHub: https://github.com/mani7204mani

---

## ⭐ If you found this project useful, consider giving it a star!
