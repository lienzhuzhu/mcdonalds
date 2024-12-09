from os import path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_FOLDER = "~/armory/mcdonalds/data/"
DATA_FILE = "McDonaldsMenuNutritionV3.csv"

def general_stats(data):
    print(data.head())
    print(data.shape)
    print(data.info())
    print(data.describe())

def main():
    raw_data = pd.read_csv(path.join(DATA_FOLDER, DATA_FILE))
    corr = raw_data.corr(numeric_only=True)
    print(corr)


if __name__ == "__main__":
    main()
