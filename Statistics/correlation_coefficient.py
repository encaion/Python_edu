# https://zhiyzuo.github.io/Pearson-Correlation-CI-in-Python/
from scipy.stats.stats import pearsonr
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")

pearsonr(df["Sepal.Length"], df["Sepal.Width"])

df.corr(method = "pearson")
df.corr(method = "kendall")
df.corr(method = "spearman")
