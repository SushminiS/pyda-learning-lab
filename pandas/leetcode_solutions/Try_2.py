# Get the Size of a DataFrame


"""players:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+"""

import pandas as pd 

players={

    "Column Name" :["player_id","name " ," age " ,"position"],

    "Type":["int","obj","int","obj"]

}

df=pd.DataFrame(players)

print(list(df.shape))

