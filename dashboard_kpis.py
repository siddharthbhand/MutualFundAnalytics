import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("\nTOTAL SCHEMES:")
print(len(fund_master))

print("\nTOTAL FUND HOUSES:")
print(fund_master["fund_house"].nunique())

print("\nTOTAL AUM (Crores):")
print(aum["aum_crore"].sum())

print("\nTOP FUND HOUSE BY AUM:")

latest_date = aum["date"].max()

latest_data = aum[aum["date"] == latest_date]

top_house = latest_data.sort_values(
    "aum_crore",
    ascending=False
)

print(top_house[["fund_house","aum_crore"]].head(5))