import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv("linear_regression_01.csv")
model = smf.ols('y ~ x', data = df)
result = model.fit()
print(result.summary())
