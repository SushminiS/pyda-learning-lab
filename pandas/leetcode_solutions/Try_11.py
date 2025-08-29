# Method Chaining

# list the names of animals that weigh strictly more than 100 kilograms.

# Return the animals sorted by weight in descending order.


import pandas as pd

animals= {
    "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]
}


df=pd.DataFrame(animals)

filtered = df[df["weight"] > 100]  # filter by weight

filtered = filtered.sort_values(by="weight", ascending=False)  # sort descending

print( filtered[["name"]])