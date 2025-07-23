from pathlib import Path

folder = Path("/Users/chloe/Desktop/Banana_project/processing_data")

for file in folder.iterdir():
    if file.is_file() and file.name.startswith("cleaned_"):
        # Remove "cleaned_" and replace spaces with underscores
        new_name = file.name.replace("cleaned_", "").replace(" ", "_")
        new_path = file.with_name(new_name)
        print(f"Renaming: {file.name} → {new_name}")
        file.rename(new_path)
