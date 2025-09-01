import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 28, 35],
    'City': ['NY', 'LA', 'NY', 'LA']
}
df = pd.DataFrame(data)

# Group by City and find average Age
avg_age_per_city = df.groupby("City")["Age"].mean()


# If you want the result back as a DataFrame (not a Series):

# df.groupby("City", as_index=False)["Age"].mean()
print(avg_age_per_city)
