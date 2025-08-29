
# Display the first 3 rows of this DataFrame.

"""DataFrame: employees
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+"""

import pandas as pd


employees={

    "Column Name" :["employee_id","name " ," department " ,"salary"],

    "Type":["int","obj","obj","int"]


}

df=pd.DataFrame(employees)

print(df.head(3))

# if want to print specific columns

print(df["Column Name"].head(3))


# If you want them as a list instead of a Series:

print(df["Column Name"].head(3).tolist()) #['employee_id', 'name', 'department']

#Select specific rows by index (e.g., row 0 and 2)

print(df.loc[[0, 2], ["Column Name", "Type"]])

# Using .iloc (row/column positions instead of labels)

print(df.iloc[[0, 2], [0, 1]])

#If you want the result as a list of lists

print(df.loc[[0, 2], ["Column Name", "Type"]].values.tolist()) #[['employee_id', 'int'], ['department', 'obj']]






