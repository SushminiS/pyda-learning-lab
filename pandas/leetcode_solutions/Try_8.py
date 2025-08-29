# Rename Columns

import pandas as pd

students={

    "id": [1, 2, 3],
    "first": ["Alice", "Bob", "Charlie"],
    "last": ["Smith", "Brown", "Davis"],
    "age": [20, 21, 22]
}

df=pd.DataFrame(students)

df=df.rename(columns={
    "id": "student_id",
    "first": "first_name",
    "last": "last_name",
    "age": "age_in_years"
    })


print(df)