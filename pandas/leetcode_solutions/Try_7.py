# Modify Columns

import pandas as pd

employees = {

    "name": ["Jack", "Piper", "Mia", "Ulysses"],
    "salary": [19666, 74754, 62509, 54866]
}

df=pd.DataFrame(employees)

df["salary"]*=2

print(df)