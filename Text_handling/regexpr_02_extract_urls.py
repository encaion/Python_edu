import re
import pandas as pd

lines = open("regexpr_example.txt").readlines()
s_sub = []
for s in lines:
    ss = re.search("http.{30,90}.jpg", s)
    if ss != None:
        s_sub.append(ss.group())
s_sub

df_imgs = pd.DataFrame({"obs": range(len(s_sub)),
                        "utl": s_sub})
df_imgs.head()
