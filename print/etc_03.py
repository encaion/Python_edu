import pandas as pd
anti = pd.read_csv("Antibiotic_70K_patinets.csv")
anti.head()

rate_mean = anti[["high_p", "age_5"]].groupby("age_5").mean()
rate_mean.sort_values(by = "high_p", ascending = False)
rate_mean.sort_values(by = "high_p", ascending = False).index[0]

anti.isna().sum().sum()

len(anti["ID"].unique()) == len(anti)

anti.head()
upper_2 = anti["total_d"].quantile(0.98)

sum(anti["total_d"] > upper_2)

anti.loc[anti["total_d"] > upper_2, "total_d"] = upper_2

import scipy.stats as ss
ss.stats.pearsonr(anti["high_p"], anti["age_5"])
