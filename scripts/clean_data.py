import pandas as pd

#Load dataset

df = pd.read_csv("data/raw/raw_data.csv")

print("First rows:")
print(df.head())

print("\nDatset info:")
print(df.info())

#standardize the columns
df.columns = df.columns.str.lower().str.replace(" ","_")
print(df.columns)

#handle missing values- frop unuseful columns
print(df.isnull().sum())
df = df.drop(columns=["symbol","terminated"])
#removing raws where the acual value is missing
df = df.dropna(subset=["value"])
print(df.columns)


#converting Date columns
df["ref_date"] = pd.to_datetime(df['ref_date'])
print("First rows:")
print(df.head())

df.to_csv("data/processed/data_clean.csv", index = False)
print("Clean dataset saved!")