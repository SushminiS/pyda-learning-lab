# Drop Duplicate Rows and keep only the first occurence.

"""DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+"""

import pandas as pd

customers = {
    "customer_id": [1, 2, 3, 4, 5, 6],
    "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
    "email": [
        "emily@example.com",
        "michael@example.com",
        "sarah@example.com",
        "john@example.com",
        "john@example.com",
        "alice@example.com"
    ]
}


df=pd.DataFrame(customers)
    
df.drop_duplicates(subset="email",keep="first",inplace=True) #inplace helpd to overwrite the same frame instead of assigning to a new df.

print(df)
