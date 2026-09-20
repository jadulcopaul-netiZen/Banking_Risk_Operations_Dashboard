import pandas as pd
from pathlib import Path

#Project root .resolve to get absolute path, and .parent to get parent directory
project_root = Path(__file__).resolve().parent.parent

# Source dataset
source_file = project_root / "data" / "archive" / "archive" / "PS_20174392719_1491204439457_log.csv"

# Load full dataset
df = pd.read_csv(source_file)

# Create reproducible random sample
sample_df = df.sample(
    n=200000,
    random_state=42
)

# Save development dataset
output_file = project_root / "data" / "bronze" / "transactions_200k_sampled.csv"
output_file.parent.mkdir(parents=True, exist_ok=True) #to create the parent directories if they don't exist

sample_df.to_csv(
    output_file,
    index=False
)

print("Sample created successfully.")
print(f"Rows: {len(sample_df)}")
print(f"Step range: {sample_df['step'].min()} -> {sample_df['step'].max()}")