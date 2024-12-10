from os import path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_FOLDER = "~/armory/mcdonalds/data/"
DATA_FILE = "mcds.csv"

def general_stats(data):
    print(data)

def main():
    mcds = pd.read_csv(path.join(DATA_FOLDER, DATA_FILE))
    print(mcds.columns)


if __name__ == "__main__":
    main()
