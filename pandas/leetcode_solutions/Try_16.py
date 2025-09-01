# You have a DataFrame df with columns Name and Score. How do you replace all scores less than 50 with 50?


import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [45, 70, 30]}
df = pd.DataFrame(data)

# Replace all scores less than 50 with 50
df["Score"] = df["Score"].clip(lower=50)


#  or  df["Score"] = df["Score"].mask(df["Score"] < 50, 50)
print(df)
