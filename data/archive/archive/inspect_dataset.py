import pandas as pd

file_path = r"C:\Users\DELL\Desktop\Luap\Data Engineering\Banking_Risk_Operations_Dashboard\Data\Archive\archive\PS_20174392719_1491204439457_log.csv"

df = pd.read_csv(
    file_path,
    nrows=5
)

print("First 5 rows:")
print(df)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)