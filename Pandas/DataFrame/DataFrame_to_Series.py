import pandas as pd
df = pd.DataFrame({'date': [20130101, 20130101, 20130102], 
                   'location': ['a', 'a', 'c']})
print(df)
print(df[df["location"] == "c"].squeeze())
