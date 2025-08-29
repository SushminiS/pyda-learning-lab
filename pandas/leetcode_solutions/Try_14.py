# Reshape data - melt
# reshape the data so that each row represents sales data for a product in a specific quarter

import pandas as pd


df = pd.DataFrame({
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
})

reshaped_df = df.melt(
    id_vars=['product'],
    var_name='quarter',
    value_name='sales'
)

print("\nReshaped DataFrame:")
print(reshaped_df)