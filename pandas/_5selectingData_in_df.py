#Selecting data in DataFrames:

"""     Name  Age  Marks
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     95

There are two main ways:"""

# By column name

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Marks": [85, 90, 95]
}

df=pd.DataFrame(data)

print(df["Age"] )      # gives a Series
print(df[["Name", "Marks"]])  # gives multiple columns as DataFrame

# 0    25
# 1    30
# 2    35
# Name: Age, dtype: int64

#       Name  Marks
# 0    Alice     85
# 1      Bob     90
# 2  Charlie     95


# By row/position

#.loc[] → label-based (row names, column names)

#.iloc[] → position-based (row numbers, column numbers)

# Using loc (labels)
print(df.loc[0, "Name"])   # Alice

# Using iloc (positions)
print(df.iloc[1, 2])       # 90