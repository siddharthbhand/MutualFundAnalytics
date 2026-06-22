import pandas as pd
import matplotlib.pyplot as plt

aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

latest_date = aum["date"].max()

latest_data = aum[aum["date"] == latest_date]

top_house = latest_data.sort_values(
    "aum_crore",
    ascending=False
)

top5 = top_house.head(5)

plt.figure(figsize=(10,5))

plt.bar(
    top5["fund_house"],
    top5["aum_crore"]
)

plt.title("Top 5 Fund Houses by AUM")

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()