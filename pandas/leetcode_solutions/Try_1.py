# create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.


"""Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+"""


import pandas as pd

student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]


df=pd.DataFrame(student_data, columns=["student_id", "age"])

print(df)