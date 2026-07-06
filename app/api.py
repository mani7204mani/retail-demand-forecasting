from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.models.predict import predict

app = FastAPI(
    title="Retail Demand Forecasting API",
    version="1.0"
)


class SalesRequest(BaseModel):
    store: int
    item: int
    year: int
    month: int
    day: int
    day_of_week: int
    day_of_year: int
    week_of_year: int
    quarter: int
    is_weekend: int
    lag_1: float
    lag_7: float
    lag_30: float
    rolling_mean_7: float
    rolling_mean_30: float
    rolling_std_7: float


@app.get("/")
def home():
    return {
        "message": "Retail Demand Forecasting API is running!"
    }


@app.post("/predict")
def predict_sales(request: SalesRequest):

    df = pd.DataFrame([request.model_dump()])

    prediction = predict(df)

    return {
        "predicted_sales": float(prediction[0])
    }