import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'Science', 'Science'],
    'Score': [85, 90, 78, 92]
})

# Create pivot table
pivot_df = df.pivot(index="Name", columns="Subject", values="Score")
print(pivot_df)
