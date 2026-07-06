import pandas as pd


def build_features(df):
    """
    Perform feature engineering for retail demand forecasting.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing:
        date, store, item, sales

    Returns
    -------
    pandas.DataFrame
        Dataframe with engineered features.
    """

    # Make a copy
    df = df.copy()

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sort data
    df = df.sort_values(["store", "item", "date"])

    # -----------------------------
    # Date Features
    # -----------------------------
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek
    df["day_of_year"] = df["date"].dt.dayofyear
    df["week_of_year"] = df["date"].dt.isocalendar().week.astype(int)
    df["quarter"] = df["date"].dt.quarter
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    # -----------------------------
    # Lag Features
    # -----------------------------
    df["lag_1"] = (
        df.groupby(["store", "item"])["sales"]
        .shift(1)
    )

    df["lag_7"] = (
        df.groupby(["store", "item"])["sales"]
        .shift(7)
    )

    df["lag_30"] = (
        df.groupby(["store", "item"])["sales"]
        .shift(30)
    )

    # -----------------------------
    # Rolling Mean Features
    # -----------------------------
    df["rolling_mean_7"] = (
        df.groupby(["store", "item"])["sales"]
        .transform(lambda x: x.shift(1).rolling(7).mean())
    )

    df["rolling_mean_30"] = (
        df.groupby(["store", "item"])["sales"]
        .transform(lambda x: x.shift(1).rolling(30).mean())
    )

    # -----------------------------
    # Rolling Standard Deviation
    # -----------------------------
    df["rolling_std_7"] = (
        df.groupby(["store", "item"])["sales"]
        .transform(lambda x: x.shift(1).rolling(7).std())
    )

    # Remove rows created by lag/rolling features
    df = df.dropna().reset_index(drop=True)

    return df