import pandas as pd
from scipy.stats import f_oneway
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = f_oneway(df["Sepal.Length"], df["Sepal.Width"], df["Petal.Length"])
print(stat)
print(p)
