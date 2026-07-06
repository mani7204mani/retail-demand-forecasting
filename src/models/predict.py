from pathlib import Path
import joblib
import pandas as pd
from src.utils.config import MODEL_PATH

print("Loading model from:", MODEL_PATH)

model = joblib.load(MODEL_PATH)


def predict(features: pd.DataFrame):
    return model.predict(features)