import pandas as pd
from pathlib import Path

# Input & output file paths
csv_path = Path("Cleaned_data/Port_list.csv")
parquet_path = csv_path.with_suffix(".parquet")

# Read CSV
df = pd.read_csv(csv_path)

# Save as Parquet
df.to_parquet(parquet_path, engine="pyarrow", index=False)

print(f"✅ Converted: {csv_path} → {parquet_path}")
