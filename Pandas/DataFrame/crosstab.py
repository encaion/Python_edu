import pandas as pd
df = pd.read_csv("bike.csv")
df.iloc[:3,:]

# creation
pd.crosstab(df["season"], df["holiday"])
pd.crosstab(df["season"], df["holiday"], margins = True)

pd.crosstab([df["season"], df["workingday"]], df["holiday"])

# proportion
pd.crosstab(df["season"], df["holiday"]).apply(lambda r: r/r.sum(), axis=0)
pd.crosstab(df["season"], df["holiday"]).apply(lambda r: r/r.sum(), axis=1)

# indexing
tab = pd.crosstab(df["season"], df["holiday"])
tab.iloc[0]

tab.iloc[1]
tab.iloc[1, :]

tab.iloc[:, 1]
