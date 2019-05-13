import pandas as pd
df = pd.read_csv("bike.csv")

df[["season", "holiday"]].drop_duplicates()
df[["season", "holiday"]].drop_duplicates(keep = "first")
df[["season", "holiday"]].drop_duplicates(keep = "last")

df[["season", "holiday"]].drop_duplicates().reset_index()
df[["season", "holiday"]].drop_duplicates().reset_index(drop = True)
