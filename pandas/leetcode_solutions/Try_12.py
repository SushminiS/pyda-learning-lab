# Reshape Data-Concatenate

import pandas as pd

df1 = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17]
})

df2 = pd.DataFrame({
    "student_id": [1, 2],
    "name": ["Leo", "Alex"],
    "age": [7, 7]
})

df=pd.concat([df1,df2],ignore_index=True) #...default axis=0

print(df)


#######################

# df=pd.concat([df1,df2],axis=1) ...columnwise join

# print(df)

#######################

"""df1 = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17],
    "place":["ernk","kochi","trsr","tvm"]
})

df2 = pd.DataFrame({
    "student_id": [1, 2],
    "name": ["Leo", "Alex"],
    "age": [7, 7]
})"""


#dfk=pd.concat([df1, df2], join="inner", ignore_index=True) ..only intersected col displayed 
#dfl=pd.concat([df1, df2], join= "inner",keys=["df1","df2"]) ..adds outer index level labelling Df source
"""       student_id     name  age
df1 0           1    Mason    8
    1           2      Ava    6
    2           3   Taylor   15
    3           4  Georgia   17
df2 0           1      Leo    7
    1           2     Alex    7"""




