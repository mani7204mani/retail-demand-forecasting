import os
import sys
from datetime import date
from datetime import datetime

import pandas as pd
import streamlit as st

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if project_root not in sys.path:
    sys.path.append(project_root)

from src.models.predict import predict
from src.utils.s3_utils import upload_prediction_history


# -------------------------------------------------------------------
# Fix imports
# -------------------------------------------------------------------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if project_root not in sys.path:
    sys.path.append(project_root)

from src.models.predict import predict

# -------------------------------------------------------------------
# Page Config
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------------------------
# Title
# -------------------------------------------------------------------
st.title("📈 Retail Demand Forecasting")

st.markdown(
"""
### Predict future retail demand using Machine Learning.

This application forecasts daily product sales using an **XGBoost Regressor** trained on historical retail data.

Use the sidebar to configure prediction inputs and click **Predict Sales**.
"""
)

# -------------------------------------------------------------------
# Sidebar Inputs
# -------------------------------------------------------------------
st.sidebar.header("Prediction Inputs")

store = st.sidebar.number_input(
    "Store",
    min_value=1,
    value=1
)

item = st.sidebar.number_input(
    "Item",
    min_value=1,
    value=1
)

selected_date = st.sidebar.date_input(
    "Select Date",
    value=date(2017, 1, 1)
)

# -------------------------------------------------------------------
# Automatically create date features
# -------------------------------------------------------------------
year = selected_date.year
month = selected_date.month
day = selected_date.day

day_of_week = selected_date.weekday()

day_of_year = selected_date.timetuple().tm_yday

week_of_year = selected_date.isocalendar().week

quarter = (month - 1) // 3 + 1

is_weekend = int(day_of_week >= 5)

# -------------------------------------------------------------------
# Advanced Features
# -------------------------------------------------------------------
with st.sidebar.expander("Advanced Features", expanded=False):

    lag_1 = st.number_input(
        "Lag 1",
        value=20.0
    )

    lag_7 = st.number_input(
        "Lag 7",
        value=18.0
    )

    lag_30 = st.number_input(
        "Lag 30",
        value=15.0
    )

    rolling_mean_7 = st.number_input(
        "Rolling Mean 7",
        value=19.0
    )

    rolling_mean_30 = st.number_input(
        "Rolling Mean 30",
        value=17.0
    )

    rolling_std_7 = st.number_input(
        "Rolling Std 7",
        value=2.5
    )

predict_button = st.sidebar.button("🚀 Predict Sales")

st.sidebar.divider()

st.sidebar.markdown("## 📌 Project Information")

st.sidebar.info(
    """
**Model:** XGBoost Regressor

**Features:** 16

**R² Score:** 0.937

**RMSE:** 7.92

**Frameworks:**
- FastAPI
- Streamlit
- Scikit-Learn
"""
)
# -------------------------------------------------------------------
# Main Layout
# -------------------------------------------------------------------
left, right = st.columns([2, 1])
# --------------------------------------------------
# Prediction History
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []
# -------------------------------------------------------------------
# Prediction
# -------------------------------------------------------------------
if predict_button:

    sample = pd.DataFrame([{

        "store": store,
        "item": item,

        "year": year,
        "month": month,
        "day": day,

        "day_of_week": day_of_week,
        "day_of_year": day_of_year,
        "week_of_year": week_of_year,

        "quarter": quarter,
        "is_weekend": is_weekend,

        "lag_1": lag_1,
        "lag_7": lag_7,
        "lag_30": lag_30,

        "rolling_mean_7": rolling_mean_7,
        "rolling_mean_30": rolling_mean_30,
        "rolling_std_7": rolling_std_7

    }])

    prediction = predict(sample)[0]
    
    from datetime import datetime

    history_file = os.path.join(project_root, "data", "prediction_history.csv")

    os.makedirs(os.path.dirname(history_file), exist_ok=True)

    history = pd.DataFrame([{
        "timestamp": datetime.now(),
        "store": store,
        "item": item,
        "date": selected_date,
        "predicted_sales": round(float(prediction), 2)
    }])

    history.to_csv(
        history_file,
        mode="a",
        header=not os.path.exists(history_file),
        index=False
    )

    upload_prediction_history(history_file)

    with left:

        st.subheader("Prediction")

        st.metric(
            label="Predicted Sales",
            value=f"{prediction:.2f} Units"
        )

        st.success("Prediction completed successfully!")

    with right:

        st.subheader("Input Summary")

        summary = pd.DataFrame({

            "Feature": [
                "Store",
                "Item",
                "Date",
                "Weekend",
                "Lag 1",
                "Lag 7",
                "Lag 30",
                "Rolling Mean 7",
                "Rolling Mean 30",
                "Rolling Std 7"
            ],

            "Value": [
                store,
                item,
                selected_date,
                is_weekend,
                lag_1,
                lag_7,
                lag_30,
                rolling_mean_7,
                rolling_mean_30,
                rolling_std_7
            ]

        })

        st.table(summary)
        with st.expander("🔍 View Model Input"):

            st.dataframe(sample)

# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------
st.markdown("---")
st.divider()

st.subheader("📋 Prediction History")

history_file = os.path.join(project_root, "data", "prediction_history.csv")

if os.path.exists(history_file):
    history = pd.read_csv(history_file)

    st.dataframe(
        history,
        use_container_width=True
    )

    csv = history.to_csv(index=False)

else:
    st.info("No prediction history available.")
    csv = ""

st.download_button(

    "⬇ Download Prediction History",

    csv,

    "prediction_history.csv",

    "text/csv"

)
st.divider()

st.subheader("📊 Feature Importance")

try:

    importance = pd.read_csv(
        "artifacts/feature_importance.csv"
    )

    st.bar_chart(
        importance.set_index("Feature")
    )

except:

    st.warning(
        "feature_importance.csv not found."
    )
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model",
        "XGBoost"
    )

with col2:
    st.metric(
        "R² Score",
        "0.937"
    )

with col3:
    st.metric(
        "RMSE",
        "7.92"
    )

st.divider()

with st.expander("📂 Dataset Information"):

    st.write("""

Dataset :
Store Item Demand Forecasting

Stores :
10

Items :
50

Training Samples :
715,500

Testing Samples :
182,500

Target :
Daily Sales

""")

st.caption(
"""
Built using

• Python

• XGBoost

• FastAPI

• Streamlit

• Scikit-Learn

Author:
Mani Shankar Reddy
"""
)