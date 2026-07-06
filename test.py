import os
import pandas as pd

project_root = os.path.abspath(os.path.dirname(__file__))

print("Project Root:", project_root)

history_file = os.path.join(project_root, "data", "prediction_history.csv")

print("Saving to:", history_file)

os.makedirs(os.path.dirname(history_file), exist_ok=True)

df = pd.DataFrame([
    {
        "name": "Mani",
        "score": 100
    }
])

df.to_csv(history_file, index=False)

print("Exists:", os.path.exists(history_file))