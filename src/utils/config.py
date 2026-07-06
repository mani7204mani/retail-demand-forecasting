from pathlib import Path

# -----------------------------
# Project Directories
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

MODEL_DIR = BASE_DIR / "models"

ARTIFACT_DIR = BASE_DIR / "artifacts"

# -----------------------------
# Model
# -----------------------------

MODEL_NAME = "xgboost_model.pkl"

MODEL_PATH = MODEL_DIR / MODEL_NAME

# -----------------------------
# Random State
# -----------------------------

RANDOM_STATE = 42

# -----------------------------
# Features
# -----------------------------

FEATURES = [
    "store",
    "item",
    "year",
    "month",
    "day",
    "day_of_week",
    "day_of_year",
    "week_of_year",
    "quarter",
    "is_weekend",
    "lag_1",
    "lag_7",
    "lag_30",
    "rolling_mean_7",
    "rolling_mean_30",
    "rolling_std_7",
]

TARGET = "sales"

APP_NAME = "Retail Demand Forecasting"

MODEL_VERSION = "1.0"

AUTHOR = "Mani Shankar Reddy"