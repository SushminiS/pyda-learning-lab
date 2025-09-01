# Filtering Data 

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Marks": [85, 90, 95]
}

df=pd.DataFrame(data)


# Students with Marks > 85
print(df[df["Marks"] > 85])

# Output:

#       Name  Age  Marks
# 1      Bob   30     90
# 2  Charlie   35     95


print(df["Marks"] > 85)


# Output:

# 0    False
# 1     True
# 2     True


print(df[df["Marks"] == 85])

# Output:

#     Name  Age  Marks
# 0  Alice   25     85


import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Score': [85, 90, 78]})

# Filter rows where Score is between 80 and 90 (inclusive)
filtered_df = df[(df["Score"] >= 80) & (df["Score"] <= 90)]
print(filtered_df)

#filtered_df = df[df["Score"].between(80, 90)]


