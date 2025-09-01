# Adding new column(using conditions and calculations)

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Marks": [85, 90, 95]
}

df=pd.DataFrame(data)

df["Grade"] = ["B", "A", "A+"]

print(df)


# Output:

#       Name  Age  Marks Grade
# 0    Alice   25     85     B
# 1      Bob   30     90     A
# 2  Charlie   35     95    A+


df["Pass"]=df["Marks"]>=90

print(df)

# Output:

#     Name  Age  Marks Grade   Pass
# 0    Alice   25     85     B  False
# 1      Bob   30     90     A   True
# 2  Charlie   35     95    A+   True


#Pandas allows math on columns directly:

df["Marks_plus_5"] = df["Marks"] + 5
print(df)

#####################
import pandas as pd

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Score': [85, 90, 78]})

# Using apply with a lambda function
df["Score"] = df["Score"].apply(lambda x: x + 5)
print(df)



# Output

#     Name    Age   Marks  Grade  Pass   Marks_plus_5
# 0    Alice   25     85     B   False      90
# 1      Bob   30     90     A   True       95
# 2  Charlie   35     95    A+   True      100