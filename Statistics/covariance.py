# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.cov.html
# https://code.i-harness.com/ko-kr/q/e9bb3e

import numpy as np
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")

np.cov(df["Sepal.Length"], df["Sepal.Width"])
np.cov(df["Sepal.Length"], df["Sepal.Width"], ddof = 0)[0][1]
