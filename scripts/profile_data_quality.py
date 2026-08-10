import pandas as pd

# ============================================================
# LOAD DATASET
# ============================================================

file_path = "data/bronze/transactions_200k_sampled.csv"

df = pd.read_csv(file_path)

# ============================================================
# MISSING VALUES
# ============================================================

print("=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ============================================================
# DUPLICATE ROWS
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

print(df.duplicated().sum())

# ============================================================
# UNIQUE VALUES PER COLUMN
# ============================================================

print("\n" + "=" * 60)
print("UNIQUE VALUES PER COLUMN")
print("=" * 60)

print(df.nunique())

# ============================================================
# FRAUD DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("FRAUD DISTRIBUTION")
print("=" * 60)

print(df["isFraud"].value_counts())

# ============================================================
# FRAUD PERCENTAGE
# ============================================================

print("\n" + "=" * 60)
print("FRAUD PERCENTAGE")
print("=" * 60)

fraud_rate = df["isFraud"].mean() * 100

print(f"{fraud_rate:.4f}%")

# ============================================================
# TRANSACTION TYPE DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("TRANSACTION TYPE DISTRIBUTION")
print("=" * 60)

print(df["type"].value_counts())

# ============================================================
# DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df.describe())