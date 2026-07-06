# 📈 Retail Demand Forecasting using Machine Learning

An end-to-end Machine Learning project for forecasting retail sales using an XGBoost Regressor. The project includes feature engineering, a FastAPI REST API, an interactive Streamlit dashboard, Docker containerization, and deployment on AWS EC2.

---
## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- XGBoost
- Scikit-Learn
- FastAPI
- Streamlit
- Docker
- AWS EC2
- AWS S3
- Joblib

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

---

# 🏗️ Project Architecture

```text
                    User
                      │
                      ▼
          Streamlit Web Dashboard
                      │
                      ▼
              XGBoost Prediction Model
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Display Prediction      Save Prediction
      to Dashboard           History (CSV)
                                      │
                                      ▼
                              Upload to AWS S3
                                      │
                                      ▼
                          Cloud Prediction Storage
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

- AWS EC2 
- AWS S3 

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


# 📷 Project Screenshots

### Dashboard

<img width="1917" height="977" alt="image" src="https://github.com/user-attachments/assets/07dcae64-2f03-41fd-a4ce-d0fbd37a7673" />
<img width="1538" height="898" alt="image" src="https://github.com/user-attachments/assets/1c8064c5-ef15-4130-8d83-2f198bce9b9b" />
<img width="1543" height="891" alt="image" src="https://github.com/user-attachments/assets/93f0c76c-248d-4dd6-a391-ec3838880897" />


### Swagger API

<img width="1667" height="817" alt="image" src="https://github.com/user-attachments/assets/d571ee8c-2607-4302-ab42-43c789760fd1" />
<img width="1607" height="968" alt="image" src="https://github.com/user-attachments/assets/c5e1dcd2-eb8b-42da-844a-e3f54c74922c" />


### Docker

<img width="1391" height="577" alt="image" src="https://github.com/user-attachments/assets/b2e3a7d7-5d98-46a0-b458-0fa761d605c3" />

---

# ☁️ AWS S3 Integration

Every prediction generated through the Streamlit dashboard is automatically stored in an AWS S3 bucket.

This enables:

- Automatic prediction history backup
- Centralized cloud storage
- Persistent records across deployments
- Easy retrieval and analysis of prediction logs
### AWS S3 Bucket

<img width="1917" height="962" alt="image" src="https://github.com/user-attachments/assets/29e1eb59-2052-48fb-bebf-8223dee030b9" />

### Prediction History Folder

<img width="1917" height="957" alt="image" src="https://github.com/user-attachments/assets/04fad017-c7b7-4c17-bf67-89b0d9308555" />


### Stored Prediction History

<img width="1911" height="958" alt="image" src="https://github.com/user-attachments/assets/326dc87c-abb6-4f88-8f44-215dfff46528" />

---

## ✅ Project Features

✔ End-to-End Machine Learning Pipeline

✔ Feature Engineering

✔ XGBoost Regression Model

✔ FastAPI REST API

✔ Interactive Streamlit Dashboard

✔ Dockerized Deployment

✔ AWS EC2 Deployment

✔ AWS S3 Prediction History Storage

✔ Prediction History Download

✔ Modular & Production-Ready Project Structure

---
## ☁️ AWS EC2 Deployment

The application is successfully deployed on an **AWS EC2 Ubuntu instance** using **Docker**.

### Live Application

```
[http://13.232.201.186:8501](http://13.232.201.186:8501/)
```


### Deployment Screenshot

<img width="1600" height="382" alt="WhatsApp Image 2026-07-06 at 5 43 09 PM" src="https://github.com/user-attachments/assets/9fa4b554-1a90-4f01-a84c-6bab0a946964" />
<img width="1637" height="827" alt="image" src="https://github.com/user-attachments/assets/eff396bb-cfeb-454f-8b8a-77b625b95d08" />
<img width="1917" height="1027" alt="image" src="https://github.com/user-attachments/assets/09955703-1cb6-4420-a3f8-846091b62893" />

---
---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/mani7204mani/retail-demand-forecasting.git
cd retail-demand-forecasting
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

The dashboard will be available at:

```
http://localhost:8501
```

### Run the FastAPI Server

```bash
uvicorn src.api:app --reload
```

Swagger UI will be available at:

```
http://127.0.0.1:8000/docs
```

### Run Using Docker

Build the Docker image

```bash
docker build -t retail-demand-forecasting .
```

Run the Docker container

```bash
docker run -p 8501:8501 retail-demand-forecasting
```

The application will be available at:

```
http://localhost:8501
```

---

# 👨‍💻 Author

**Mani Shankar Reddy**

GitHub: https://github.com/mani7204mani

---

## ⭐ If you found this project useful, consider giving it a star!
