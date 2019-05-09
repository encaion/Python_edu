import pandas as pd
df = pd.read_csv("bike.csv")
df.to_json(r"bike.json", orient = "records")

df = pd.read_json("bike.json")
df.head()
