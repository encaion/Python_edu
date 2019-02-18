import pandas as pd
df = pd.read_csv("diamonds.csv")
df["clarity_num"] = df["clarity"].str.extract("([A-Z])", expand = True)
df.head()

df_sub = df.loc[df["cut"].str.contains("^P", regex = True), :]
df_sub["cut"].value_counts()

dd = df["clarity"].str.replace("[A-Z]", "")
dd.unique()
type(dd)
