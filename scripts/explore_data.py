import pandas as pd

df = pd.read_csv("raw_data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

