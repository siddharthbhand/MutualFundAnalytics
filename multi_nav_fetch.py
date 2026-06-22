import requests
import pandas as pd
import os

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{fund_name}.csv"

        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed for {fund_name}")