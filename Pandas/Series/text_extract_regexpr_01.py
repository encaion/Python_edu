import pandas as pd
df = pd.DataFrame({"aa": [1, 2, 3],
                   "bb": ["[product]apple", "let's[go]", "zzz"]})
print(df)

df.loc[:, "cc"] = df["bb"].str.extract(pat = "\[(.*?)\]")[0]
print(df)

