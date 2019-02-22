import pandas as pd 
import numpy as np

import sklearn.metrics as skm
from sklearn.linear_model import LogisticRegression as lr

df = pd.read_csv("bank.csv", sep = ";")
df.head()

set(df.y)

df["y"] = df["y"].replace("no", 0).replace("yes", 1)
set(df.y)

df.head()

jobs = df["job"].value_counts(True)
jobs = jobs[jobs < 0.05].index
jobs

for s in jobs:
    df["job"] = df["job"].replace(s, "etc")

df["job"].value_counts(True)
df["job"].value_counts(True)["etc"].round(3)

dummy_job = pd.get_dummies(df["job"], prefix = "job")
dummy_job.head()

df.columns

df2 = df[["y", "age", "balance", "duration", "previous"]]
df2.head()

df2 = pd.concat([df2, dummy_job], axis = 1)
df2.columns

df2["balance"].describe()

df2["is_minus"] = np.where(df2["balance"] < 0, 1, 0)

df2.loc[df2["balance"] <= 0, "balance"] = -1
df2["balance"] = (df2["balance"] // 5000) + 1
df2["balance"].value_counts()

model = lr().fit(df2.iloc[:, 1:], df2["y"])
model.predict(df2.iloc[:3, 1:])
predict = model.predict_proba(df2.iloc[:, 1:])[:, 1]

df_result = pd.DataFrame({"train": df2["y"],
                          "pred": np.where(predict >= 0.5, 1, 0)})

df_result

skm.accuracy_score(df_result.iloc[:, 0], df_result.iloc[:, 1])
skm.recall_score(df_result.iloc[:, 0], df_result.iloc[:, 1])
skm.roc_auc_score(df_result.iloc[:, 0], predict)
