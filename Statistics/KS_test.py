# 2 sample Kolmogorov Smirnov test
import pandas as pd
from scipy.stats import ks_2samp
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = ks_2samp(df["Sepal.Length"], df["Sepal.Width"])
print(stat)
print(p)
