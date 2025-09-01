import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Score': [85, 90, 78]})

# Get row with maximum score
max_row = df.loc[df["Score"].idxmax()] 
print(max_row)  # result a series


max_row_df = df.loc[[df["Score"].idxmax()]]
print(max_row_df)   # result a df

