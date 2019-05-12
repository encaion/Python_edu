import pandas as pd
df = pd.read_csv("bike.csv")
df.iloc[:3,:]

pd.crosstab(df["season"], df["holiday"])
pd.crosstab(df["season"], df["holiday"], margins = True)
pd.crosstab(df["season"], df["holiday"]).apply(lambda r: r/r.sum(), axis=0)
pd.crosstab(df["season"], df["holiday"]).apply(lambda r: r/r.sum(), axis=1)
