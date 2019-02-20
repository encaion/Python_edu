df2 = pd.DataFrame({"year": [2014, 2015], 
                    "quarter": ["q1", "q2"]})
df2.dtypes

df2["year"] = df2["year"].astype(str)
df2.dtypes

df2["period"] = df2[["year", "quarter"]].apply(lambda x: " ".join(x), axis = 1)
df2
