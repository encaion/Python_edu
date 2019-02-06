import pandas as pd
from scipy.stats import shapiro
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = shapiro(df["Sepal.Length"])
print(stat)
print(p)
