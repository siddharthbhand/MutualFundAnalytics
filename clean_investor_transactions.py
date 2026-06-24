import pandas as pd

# Load data
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(
    subset=["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"].isin(valid_types)
]

# Amount validation
df = df[
    df["amount_inr"] > 0
]

# Standardize KYC Status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = [
    "Verified",
    "Pending"
]

df = df[
    df["kyc_status"].isin(valid_kyc)
]

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print(
    "Saved: data/processed/investor_transactions_clean.csv"
)