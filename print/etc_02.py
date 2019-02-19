import pandas as pd
df = pd.read_csv("hotel_booking_train_1m.csv")
df.head(2)

df.columns

pd.crosstab(df.channel, df.is_booking)
cross = pd.crosstab(df.channel, df.is_booking, normalize = "index")
cross.loc[cross.iloc[:, 1] == cross.iloc[:, 1].max(), :].index
cross.iloc[:, 1].max().round(3)

cross["channel"] = cross.index
cross.head()
