import pandas as pd
from sklearn.linear_model import LinearRegression as lm
import statsmodels.formula.api as smf
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

model1 = smf.ols("casual ~ " + features, data = df)
print(model1.fit().summary())

X_df = df.iloc[:, 1:-3]
model2 = lm().fit(X_df, y)
model2.predict(X_df.iloc[:3, :])
