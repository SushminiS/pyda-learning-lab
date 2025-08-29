"""Inspecting DataFrames

When working with large datasets, we often want to quickly inspect them. Pandas has some very handy functions:
"""
# df.head()   # Shows first 5 rows
# df.tail()   # Shows last 5 rows
# df.shape    # Shows (rows, columns)
# df.info()   # Shows summary of columns and datatypes
# df.describe() # Shows statistics (mean, min, max, etc.) for numeric columns


"""     Name  Age  Marks
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     95

What will df.shape return?

And if we call df.head(2), what will be displayed?"""

# df.shape → (3, 3) → meaning 3 rows and 3 columns.

# df.head(2) → shows the first 2 rows:

#       Name  Age  Marks
# 0    Alice   25     85
# 1      Bob   30     90