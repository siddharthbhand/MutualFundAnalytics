import pandas as pd

# NAV History Load
df = pd.read_csv("data/raw/02_nav_history.csv")

# Date Convert
df["date"] = pd.to_datetime(df["date"])

performance = []

# Calculate Returns For Every Fund
for amfi_code in df["amfi_code"].unique():

    fund_nav = df[df["amfi_code"] == amfi_code].copy()

    # Oldest to Latest
    fund_nav = fund_nav.sort_values("date")

    start_nav = fund_nav.iloc[0]["nav"]
    end_nav = fund_nav.iloc[-1]["nav"]

    return_pct = (
        (end_nav - start_nav)
        / start_nav
    ) * 100

    performance.append([
        amfi_code,
        round(start_nav, 2),
        round(end_nav, 2),
        round(return_pct, 2)
    ])

# Create Result DataFrame
result = pd.DataFrame(
    performance,
    columns=[
        "amfi_code",
        "start_nav",
        "end_nav",
        "return_pct"
    ]
)

# Fund Master Load
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# Merge Scheme Names
result = result.merge(
    fund_master[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code",
    how="left"
)

# Sort Best Returns First
result = result.sort_values(
    "return_pct",
    ascending=False
)

print("\nTOP 10 PERFORMING FUNDS\n")

print(
    result[
        [
            "scheme_name",
            "start_nav",
            "end_nav",
            "return_pct"
        ]
    ].head(10)
)

# Save Output
result.to_csv(
    "data/processed/top_performing_funds.csv",
    index=False
)

print("\nFile Saved Successfully")
print("data/processed/top_performing_funds.csv")