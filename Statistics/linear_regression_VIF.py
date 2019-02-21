import pandas as pd
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
df = pd.read_csv("bike.csv")
df.head()

features = "+".join(df.columns[1:-3])
y, X = dmatrices("casual ~ " + features, df, return_type = "dataframe")

df_vif = pd.DataFrame()
df_vif["VIF"] = [vif(X.values, i) for i in range(X.shape[1])]
df_vif["features"] = X.columns
df_vif
