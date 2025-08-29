# Fill missing values

import pandas as pd

data = {
    "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
    "quantity": [None, None, 779, 849],
    "price": [135, 821, 9319, 3051]
}

df = pd.DataFrame(data)


df["quantity"] = df["quantity"].fillna(0)

print(df)