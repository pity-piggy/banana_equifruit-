import pandas as pd
import json
import numpy as np
from pathlib import Path


def pandas_dtype_to_json(dtype):
    """Map pandas dtypes to JSON schema-friendly types."""
    if pd.api.types.is_string_dtype(dtype) or pd.api.types.is_object_dtype(dtype):
        return "string"
    elif pd.api.types.is_integer_dtype(dtype):
        return "integer"
    elif pd.api.types.is_float_dtype(dtype):
        return "number"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "date"
    else:
        return "string"


def generate_schema(df, table_name, descriptions=None):
    """Generate a schema dict for a DataFrame."""
    schema = {
        table_name: {
            "row_count": int(df.shape[0]),
            "column_count": int(df.shape[1]),
            "columns": []
        }
    }

    for col in df.columns:
        col_dtype = df[col].dtype
        json_type = pandas_dtype_to_json(col_dtype)
        example = df[col].dropna().iloc[0] if not df[col].dropna().empty else None
        if isinstance(example, (pd.Timestamp, pd.DatetimeIndex)):
            example = str(example)
        elif isinstance(example, (np.integer, int)):
            example = int(example)
        elif isinstance(example, (np.floating, float)):
            example = float(example)
        elif isinstance(example, str):
            example = example.replace("\r", " ").replace("\n", " ").strip()

        schema[table_name]["columns"].append({
            "name": col,
            "type": json_type,
            "description": descriptions.get(col, "") if descriptions else "",
            "example": example
        })
    return schema


def load_descriptions(desc_path):
    """Load optional column descriptions from JSON."""
    if desc_path and Path(desc_path).exists():
        with open(desc_path) as f:
            return json.load(f)
    return {}


def main(input_folder, output_path="all_tables.schema.json", desc_path=None):
    """Process all CSVs in folder & output combined schema JSON."""
    folder = Path(input_folder)
    all_schemas = {}
    descriptions = load_descriptions(desc_path)

    for csv_file in folder.glob("*.csv"):
        table_name = csv_file.stem
        print(f"🔷 Processing: {csv_file} → table_name: {table_name}")
        df = pd.read_csv(csv_file)

        schema = generate_schema(df, table_name, descriptions)
        all_schemas.update(schema)

    with open(output_path, "w") as f:
        json.dump(all_schemas, f, indent=4, ensure_ascii=False, default=str)

    print(f"✅ Combined schema written to: {output_path}")


if __name__ == "__main__":
    # 🔷 Change the path to your processing_data folder if needed
    main(input_folder="processing_data", output_path="all_tables.schema.json", desc_path=None)
