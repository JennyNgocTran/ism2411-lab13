# Reflection Questions
# 1. A boolean filter evaluates a condition for every row, and discards the Falses.
# 2. Single brackets return a flat 1D Series. Double brackets returns a 2D single-column DataFrame. 
# 3. Using pandas allows you to work with much more data faster than Excel.

print("--- Exercise 1: Load it ---")

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

# Inspection commands
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("--- Exercise 2: Filter by region ---")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print("--- Exercise 3: Top 5 by revenue ---")

top_5 = df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("--- Exercise 4: Two-condition filter ---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

print("--- Exercise 5: A new column ---")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print("--- Exercise 6: Unique values ---")

print(df['region'].unique())
# tells us IF we operate in a region
print(df['region'].value_counts())
# tells us HOW MUCH business we do there
# .plot

print("--- Exercise 7: Select columns ---")

df_subset = df[['region', 'product', 'revenue']]

print(df_subset.shape) # (5000,3)

print("--- Exercise 8: Save ---")

df.to_csv('data/explored.csv', index=False) # index=False cleans data