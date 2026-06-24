import pandas as pd

# Load data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing numeric values
df = df.dropna(subset=numeric_cols)

# Expense ratio validation
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print(
    "Saved: data/processed/scheme_performance_clean.csv"
)