import pandas as pd
df=pd.read_csv('data_modified.csv')
print(df.isnull().sum())
df = df.dropna()