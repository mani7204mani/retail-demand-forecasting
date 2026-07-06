from src.utils.config import RAW_DATA_DIR
import pandas as pd

def load_data():
   

    print("Loading from:", RAW_DATA_DIR)

    train = pd.read_csv(RAW_DATA_DIR / "train.csv")
    test = pd.read_csv(RAW_DATA_DIR / "test.csv")

    train["date"] = pd.to_datetime(train["date"])
    test["date"] = pd.to_datetime(test["date"])

    return train, test