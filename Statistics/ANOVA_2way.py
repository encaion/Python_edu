# https://partrita.github.io/posts/ANOVA-python/

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
df = pd.read_csv("diamonds.csv")
formula = "price ~ C(cut) + C(clarity)"
lm = ols(formula, df).fit()
print(anova_lm(lm))
