import numpy as np
import pandas as pd

df = pd.read_csv("class_scores.csv")

df.head()

df.columns
df_sub = df.loc[df["grade"] == 2, :]
df_sub = df.iloc[:, np.r_[:2, 4:9]]
df_sub.head()

df_mean = pd.DataFrame({"Stu_ID": df_sub["Stu_ID"],
                        "score_avg": df_sub.iloc[:, 2:].mean(1)})
df_mean.head()

#df_mean.to_csv("")


score_min = df_sub.agg("min")
score_max = df_sub.agg("max")
score_std  = df_sub.agg("std")
score_stat = pd.DataFrame({"subject": score_std.index,
                           "min": score_min, 
                           "max": score_max,
                           "std": score_std})
score_stat.set_index(np.arange(5))
score_stat.head()
