# scipy.stats.bartlett
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bartlett.html
# scipy.stats.fligner
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.fligner.html
# scipy.stats.levene
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html

# levene
import pandas as pd
from scipy.stats import levene
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = levene(df["Sepal.Length"], df["Sepal.Width"])
print(stat)
print(p)

# https://www.johndcook.com/blog/2018/05/16/f-bartlett-levene/
