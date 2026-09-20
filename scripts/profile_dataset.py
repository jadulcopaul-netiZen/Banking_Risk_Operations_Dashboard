import pandas as pd
from pathlib import Path

# ============================
# Load Dataset
# ============================

file_path = Path(__file__).resolve().parent.parent / "data" / "bronze" / "transactions_200k_sampled.csv"

df = pd.read_csv(file_path  )

# ============================
# Dataset Overview
# ============================

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("COLUMNS")
print("=" * 60)
print(df.columns.tolist())

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("SAMPLE ROWS")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("MEMORY USAGE")
print("=" * 60)
print(df.memory_usage(deep=True))

print("\nTotal Memory (MB):")
print(round(df.memory_usage(deep=True).sum() / 1024**2, 2))