import pandas as pd
import statsmodels.api as sm
import numpy as np
df = pd.read_csv("logistic_regression_01.csv")

dummy_ranks = pd.get_dummies(df["rank"], prefix = "rank")
df_bind = df.drop("rank", axis = 1).join(dummy_ranks.loc[:, "rank_2":])

train_cols = df_bind.columns[1:]
model = sm.Logit(df_bind["admit"], df_bind.drop("admit", axis = 1))
result = model.fit()
result.summary()

# odds ratio
np.exp(result.params)
