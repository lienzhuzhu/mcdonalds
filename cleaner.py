import pandas as pd

# Load the dataset
file_path = "./data/mcds.csv"  # Adjust the file path as needed
mcds = pd.read_csv(file_path)

# Rename columns to simpler names
mcds.columns = [
    "item",
    "calories",
    "calories_from_fat",
    "total_fat_g",
    "saturated_fat_g",
    "trans_fat_g",
    "cholesterol_mg",
    "sodium_mg",
    "carbs_g",
    "fiber_g",
    "sugars_g",
    "protein_g",
    "weight_watchers_points"
]

# Save the renamed dataset to a new file for use in R or Python
output_file = "./data/mcds_clean.csv"
mcds.to_csv(output_file, index=False)

print(f"Renamed columns and saved the file to {output_file}")
