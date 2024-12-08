from os import path

import numpy as np
import pandas as pd


DATA_FOLDER = "~/armory/mcdonalds/data/"
DATA_FILE = "McDonaldsMenuNutritionV3.csv"


def main():
    raw_data = pd.read_csv(path.join(DATA_FOLDER, DATA_FILE))
    print(raw_data.columns)


if __name__ == "__main__":
    main()
