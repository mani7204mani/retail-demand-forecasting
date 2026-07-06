import numpy as np
import pandas as pd

import json
from pathlib import Path
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_model(y_true, y_pred):
    """
    Evaluate regression model performance.
    """

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    metrics = {
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4),
        "R2": round(r2, 4)
    }
    ARTIFACT_DIR = Path("artifacts")
    ARTIFACT_DIR.mkdir(exist_ok=True)

    with open(ARTIFACT_DIR / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("=" * 40)
    print("Model Evaluation")
    print("=" * 40)

    for key, value in metrics.items():
        print(f"{key}: {value}")

    return metrics