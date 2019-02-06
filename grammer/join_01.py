import pandas as pd
df_list = pd.read_csv("join_list.csv", encoding = "CP949")
df_room = pd.read_csv("join_room.csv", encoding = "CP949")
df_list.head(2)
df_room.head(2)

df_list.join(df_room, how = "left")

df_list.join(df_room, how = "inner")
