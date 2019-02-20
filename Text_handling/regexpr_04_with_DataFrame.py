import pandas as pd

df = pd.read_csv("diamonds.csv")
df.head()

df_sub = df.loc[df["cut"].str.contains("m$"), :]
df_sub.head()

df_sub["cut"].unique()[0]
