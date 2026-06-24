import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Forward fill NAV within each fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(
    "Saved: data/processed/nav_history_clean.csv"
)