import pandas as pd
df = pd.read_csv("bike.csv")

df.loc[:, "year"] = pd.DatetimeIndex(df.datetime).year

df.loc[:, "datetime"] = pd.to_datetime(df.loc[:, "datetime"])
df.loc[:, "year"] = df['datetime'].dt.year
df.loc[:, "wday"] = df['datetime'].dt.weekday
df.head()
