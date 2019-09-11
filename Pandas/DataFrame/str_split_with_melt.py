import pandas as pd
df = pd.DataFrame({"col1": ["pearson1", "person2"],
                   "col2": [1231, 2323],
                   "col3": ["1월 11일", "1월 12일"],
                   "col4": ["red|blue", "red|black"]})
df_split = df["col4"].str.split("\|", expand = True)
df = pd.concat([df.iloc[:, :-1], df_split], axis = 1)
df.melt(id_vars = ["col1", "col2", "col3"])
