from src.data.load_data import load_data
from src.features.build_features import build_features
from src.models.evaluate import evaluate_model
from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import pandas as pd
import numpy as np
import joblib
from src.utils.logger import logger
from src.utils.config import FEATURES, TARGET
from src.utils.config import RANDOM_STATE
# -------------------------
# Load Data
# -------------------------
train, test = load_data()

# -------------------------
# Feature Engineering
# -------------------------
train = build_features(train)

# -------------------------
# Train/Test Split
# -------------------------
train_df = train[train["date"] < "2017-01-01"].copy()
test_df = train[train["date"] >= "2017-01-01"].copy()



X_train = train_df[FEATURES]
y_train = train_df[TARGET]

X_test = test_df[FEATURES]
y_test = test_df[TARGET]

# -------------------------
# Train Model
# -------------------------
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=RANDOM_STATE,
    objective="reg:squarederror"
)

logger.info("Training started")
print("Training started...")
model.fit(X_train, y_train)
importance = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

importance.to_csv(
    "artifacts/feature_importance.csv",
    index=False
)

print("Feature importance saved!")

# -------------------------
# Prediction
# -------------------------
predictions = model.predict(X_test)

metrics = evaluate_model(y_test, predictions)

# -------------------------
# Save Model
# -------------------------
joblib.dump(model, "models/xgboost_model.pkl")

logger.info("Model saved successfully")
print("Model saved successfully!")