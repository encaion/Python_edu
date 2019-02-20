import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("bike_weather.csv")
df = df.iloc[:10, :4]
df

df["hour"] = df["hour"].astype(str)
df.dtypes

# 1
df["time"] = df[["date", "hour"]].apply(lambda x: ' '.join(x), axis = 1)
df["time"] = df["time"].apply(lambda x: dt.strptime(x, "%Y-%m-%d %H"))

# 2
df["time"] = df[["date", "hour"]].apply(lambda x: dt.strptime(' '.join(x), "%Y-%m-%d %H"), axis = 1)

# ※ to_datetime()

# 3
df["time"] = df["date"].str.cat(df["hour"], " ")

df["hour"].str.replace("[0-9]", "@")
