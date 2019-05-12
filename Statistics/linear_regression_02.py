import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv("bike.csv")
df.head()

df["datetime"] = pd.to_datetime(df["datetime"])
# df["wday"] = df["datetime"].dt.day_name()
df["wday"] = df["datetime"].dt.dayofweek

# One Hot Encoding: weekday
# dummy_wday = pd.get_dummies(df["wday"], prefix = "wday")
dummy_wday = pd.get_dummies(df["wday"], prefix = "wday", drop_first = True)
dummy_wday.head()

X_sub = df[["season", "holiday", "workingday", "temp", "humidity"]]
X = pd.concat([X_sub, dummy_wday], axis = 1)
X.head()

Y = df["casual"]

model = smf.OLS(Y, X).fit()
model.summary()
