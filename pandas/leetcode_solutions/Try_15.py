#Rename column

import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [24, 30], 'City': ['NY', 'LA']}
df = pd.DataFrame(data)

# Rename column City to Location
df = df.rename(columns={"City": "Location"})
print(df)
