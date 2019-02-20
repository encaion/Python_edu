import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm as aov

df = pd.read_csv("Altman_910.csv")
df.boxplot(column = "folic", by = "group")

# scipy ver.
f_stat, p_val = stats.f_oneway(df.loc[df["group"] == 1, "folic"],
                               df.loc[df["group"] == 2, "folic"],
                               df.loc[df["group"] == 3, "folic"])
f_stat
p_val

# statmodel ver.
model = ols('folic ~ C(group)', df).fit()
print(aov(model))
