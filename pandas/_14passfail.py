import pandas as pd
import numpy as np

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Score': [85, 40, 92]})

# Create Result column
df["Result"] = np.where(df["Score"] >= 50, "Pass", "Fail")
print(df)
