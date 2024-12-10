import pandas as pd
import re
import csv

# Load the dataset
file_path = "./data/mcds.csv"  # Adjust the file path as needed
mcds = pd.read_csv(file_path, encoding="utf-8")

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


# Clean up item names by removing trademark symbols
def clean_item_name(item_name):
    # Remove ™ and ® symbols
    item_name = re.sub(r'\n', ' ', item_name)
    return re.sub(r'[™®]', '', item_name)

# Apply the cleaning function to the item column
mcds['item'] = mcds['item'].apply(clean_item_name)

# Save the cleaned and renamed dataset to a new file
output_file = "./data/mcds_clean.csv"
mcds.to_csv(output_file, index=False)


print(f"Renamed columns and saved the file to {output_file}")
