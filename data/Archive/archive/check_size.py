import pandas as pd

file_path = r"C:\Users\DELL\Desktop\Luap\Data Engineering\Banking_Risk_Operations_Dashboard\Data\Archive\archive\PS_20174392719_1491204439457_log.csv"

df = pd.read_csv(
    file_path,
    nrows=150000
)

print("Sample rows:", len(df))

print("\nMemory usage:")
print(df.memory_usage(deep=True))

print("\nTotal memory:")
print(df.memory_usage(deep=True).sum() / 1024**2, "MB")