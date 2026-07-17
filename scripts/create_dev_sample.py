import pandas as pd

# Source dataset
source_file = r"Data\Archive\archive\PS_20174392719_1491204439457_log.csv"

# Load full dataset
df = pd.read_csv(source_file)

# Create reproducible random sample
sample_df = df.sample(
    n=200000,
    random_state=42
)

# Save development dataset
output_file = r"Data\transactions_200k_sampled.csv"

sample_df.to_csv(
    output_file,
    index=False
)

print("Sample created successfully.")
print(f"Rows: {len(sample_df)}")
print(f"Step range: {sample_df['step'].min()} -> {sample_df['step'].max()}")