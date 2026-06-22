import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data.keys())

print(data["meta"])

print("\nTotal NAV Records:")
print(len(data["data"]))

print("\nFirst NAV Record:")
print(data["data"][0])

import pandas as pd

df = pd.DataFrame(data["data"])

df.to_csv(
    "data/raw/live_nav.csv",
    index=False
)

print("\nCSV Saved Successfully")