import pandas as pd
df = pd.DataFrame({"aa": [1, 2, 2, 1, 3, 3],
                   "bb": [5, 6, 7, 8, 9, 9]})
                   
for n in set(df["aa"]):
    globals()["df_" + str(n)] = df[df["aa"] == n] 
    
df_1
