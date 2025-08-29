import pandas as pd

s = pd.Series([85, 90, 95], index=["Math", "Science", "English"])

"""What value will s["Science"] return?

And what about s[0]?

s["Science"] → 90 (because we’re using the label "Science")

s[0] → 85 (because we’re using the position/index 0)

That shows you can access Series values either by label or by position."""


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Marks": [85, 90, 95]
}
df = pd.DataFrame(data)
print(df)

# Output:

#       Name  Age  Marks
# 0    Alice   25     85
# 1      Bob   30     90
# 2  Charlie   35     95

print(df["Age"])

# 0    25
# 1    30
# 2    35
# Name: Age, dtype: int64




"""
What will df["Age"][1] return?

And what will df["Name"][2] return?
"""

# df["Age"][1] → 30 (second row in the Age column, since index starts at 0).

# df["Name"][2] → Charlie (third row in the Name column).

# 🔑 Recap:

# You can access DataFrame columns like df["Age"], which itself is a Series.

# From there, you can index into rows, like df["Age"][1].