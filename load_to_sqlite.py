import pandas as pd
from sqlalchemy import create_engine

# SQLite Database
engine = create_engine(
    "sqlite:///sql/bluestock_mf.db"
)

print("Database Connected")

# Load cleaned files
nav_df = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

performance_df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

transactions_df = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

# Dimension Table
dim_fund = performance_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
].drop_duplicates()

# Load tables

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")

print("\nRow Counts")

print("dim_fund:", len(dim_fund))
print("fact_nav:", len(nav_df))
print("fact_performance:", len(performance_df))
print("fact_transactions:", len(transactions_df))