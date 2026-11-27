
import json
import pandas as pd
from pathlib import Path

# File paths
folder_json = Path("datasets/phase_1_1day/raw")
folder_csv = Path("datasets/phase_1_1day/processed")

json_path = folder_json/ "1day_dataFirebase.json"
csv_path = folder_csv / "DHT22_Dataset.csv"

# Read JSON file
with open(json_path, "r", encoding="utf-8") as file:
    firebase_data = json.load(file)

# Extract history records
history = firebase_data["02_history"]

# Convert JSON into DataFrame
data = pd.DataFrame([
    {
        "record_id": record_id,
        "humidity": values.get("humidity"),
        "status": values.get("status"),
        "temperature": values.get("temperature"),
        "timestamp": values.get("timestamp")
    }
    for record_id, values in history.items()
])

# Sort by timestamp
data = data.sort_values("timestamp")

# Create CSV file
data.to_csv(csv_path, index=False)
