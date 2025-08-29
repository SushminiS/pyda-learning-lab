# select the name and age of the student with student_id = 101.

"""Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+"""

import pandas as pd

students ={

    "student_id":[101,53, 128, 3],
    "name":["ul","wl","hn","hn"],
    "age":[13,10,6,11]
}


df=pd.DataFrame(students)

print(df.loc[df["student_id"]==101 ,["name","age"]])

 