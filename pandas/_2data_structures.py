import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40])
print(s)

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)

"""Output:


0    10
1    20
2    30
3    40
dtype: int64


      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35

✨ Key idea:
A Series has data + index.

A DataFrame is made up of multiple Series (like columns)."""

#Customized Indexing

s = pd.Series([100, 200, 300], index=["A", "B", "C"])

print(s)

"""Output:

A    100
B    200
C    300
dtype: int64
👉 This is powerful because now you can access data by a meaningful label (like names, dates, categories) instead of just numbers."""