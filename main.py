from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "forestfires.csv"
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)
RANDOM_STATE = 42

df = pd.read_csv(DATA_PATH)

print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nColumn types:\n", df.dtypes)
print("\nMissing values per column:\n", df.isna().sum())
print("\nSummary statistics:\n", df.describe().T)

zero_count = (df["area"] == 0).sum()
print(f"\nFires with area = 0: {zero_count} of {len(df)} ({zero_count / len(df):.1%})")