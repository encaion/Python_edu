import pandas as pd

df = pd.read_csv("hotel_booking_train_1m.csv")
df.head(2)
df.shape
df.columns

df.rename(columns = {"user_location_country": "country",
                     "user_location_city": "city"}, inplace = True)

df_co = df[["country", "city"]].groupby("country").agg(lambda x: len(set(x)))
df_co 

def uni(x):
    return len(set(x))

df_co = df[["country", "city"]].groupby("country").agg(lambda x: len(set(x)))
df_co = df[["country", "city"]].groupby("country").agg(uni)

len(df.loc[df["country"] == 0, "city"].unique())

site_counts = df["site_name"].value_counts()
site_counts[:10].index

df_sub = df.loc[df["site_name"].isin(site_counts[:10].index), :]
len(df_sub["site_name"].unique())


df_sub.head()
df_sub.columns
book_ratio = pd.crosstab(df_sub["srch_adults_cnt"],
                         df_sub["is_booking"],
                         normalize = True)
book_ratio.loc[book_ratio[1] == max(book_ratio[1]), :].index[0]



