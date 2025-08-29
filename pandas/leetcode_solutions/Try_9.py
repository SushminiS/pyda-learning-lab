# Change DataTypes

import pandas as pd

students = {
    "student_id": [1, 2],
    "name": ["Ava", "Kate"],
    "age": [6, 15],
    "grade": [73.0, 87.0]
}

df=pd.DataFrame(students)
    
df["grade"]=df["grade"].astype(int)

print(df)