import pandas as pd

df = pd.DataFrame({'City': ['New York', 'Los Angeles', 'Chicago', 'New York']})

# Count occurrences of each city
city_counts = df["City"].value_counts()
print(city_counts)
