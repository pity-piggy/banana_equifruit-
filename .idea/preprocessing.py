import pandas as pd
import numpy as np
import os

# folder with raw CSVs
input_folder = "Accounting"
output_folder = "Cleaned_data"

os.makedirs(output_folder, exist_ok=True)


def clean_file(filepath, output_path):
    print(f"Processing: {filepath}")
    df = pd.read_csv(filepath, encoding="cp1252")

    # drop all-NaN columns
    cols_to_drop_nan = [col for col in df.columns if df[col].count() == 0]
    df_cleaned = df.drop(columns=cols_to_drop_nan)
    print(f"  Dropped all-NaN columns: {cols_to_drop_nan}")

    # drop single-value columns:
    #   → numeric & only 0
    #   → categorical & only one unique value
    cols_single_value = []
    for col in df_cleaned.columns:
        unique_vals = df_cleaned[col].nunique()
        dtype = df_cleaned[col].dtype

        if np.issubdtype(dtype, np.number):
            if unique_vals == 1 and df_cleaned[col].iloc[0] == 0:
                cols_single_value.append(col)
        else:
            if unique_vals == 1:
                cols_single_value.append(col)

    df_final = df_cleaned.drop(columns=cols_single_value)
    print(f"  Dropped single-value columns (numeric=0 or categorical=single): {cols_single_value}")

    df_final.to_csv(output_path, index=False)
    print(f"    Saved cleaned file to: {output_path}\n")

# process each CSV in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_folder, filename)

        # replace spaces in filename with underscores
        cleaned_filename = filename.replace(" ", "_")

        output_path = os.path.join(output_folder, cleaned_filename)
        clean_file(input_path, output_path)


print(" All files processed.")
