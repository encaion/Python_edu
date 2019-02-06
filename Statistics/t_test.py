# https://datascienceschool.net/view-notebook/14bde0cc05514b2cae2088805ef9ed52/
# https://stackoverflow.com/questions/15984221/how-to-perform-two-sample-one-tailed-t-test-with-numpy-scipy

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html

# 2 indipendent sample t-test with equal variance
import pandas as pd
from scipy.stats import ttest_ind
df = pd.read_excel("iris_xlsx.xlsx")
stat, p = ttest_ind(df["Sepal.Length"], df["Sepal.Width"], equal_var = True)
print(stat)
print(p)
