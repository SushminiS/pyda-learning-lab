# Removing Data

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Marks": [85, 90, 95],
    "Double_Age": [50, 60, 70]
}

df=pd.DataFrame(data)


# Drop column

df = df.drop("Double_Age", axis=1)

# Drop row with index 0
df = df.drop(0, axis=0)

print(df)

# Output

#      Name  Age  Marks
# 1      Bob   30     90
# 2  Charlie   35     95

# After dropping, you usually reassign back to df (since drop() by default returns a new DataFrame without changing the original unless inplace=True)




# To drop rows where Age is missing (NaN), you should use:


import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, np.nan, 28], 'City': ['NY', 'LA', 'SF']}
df = pd.DataFrame(data)

# Drop rows where Age is missing
df = df.dropna(subset=["Age"])
print(df)