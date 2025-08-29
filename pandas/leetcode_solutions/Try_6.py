# Drop Missing Data

import pandas as pd

students={

    "student_id": [32, 217, 779, 849],

    "name": ["Piper", None, "Georgia", "Willow"],

    "age": [5, 19, 20, 14]
}
df=pd.DataFrame(students)

df.dropna(subset="name",inplace=True)

print(df)