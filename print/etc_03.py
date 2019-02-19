import pandas as pd
df = pd.read_csv("traffic_highway.csv")
df["max"] = df.iloc[:, 2:7].max(1)

df.loc[df["max"] == df["max"].max(), ["date", "StartPoint"]]

df.loc[:, ["StartPoint", "max"]].groupby("StartPoint").max()

df["sum"] = df.iloc[:, 2:7].sum(1)
df.loc[df["sum"] == df["sum"].max(), ["date", "StartPoint"]]

