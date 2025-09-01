import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 90, 75]})

# Merge on ID (inner join by default)
merged_df = pd.merge(df1, df2, on="ID")
print(merged_df)