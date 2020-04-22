import pandas as pd
df_list = pd.read_csv("join_list.csv", encoding = "CP949")
df_room = pd.read_csv("join_room.csv", encoding = "CP949")
df_list.head(2)
df_room.head(2)

# index based join.
df_list.join(df_room, how = "left")
df_list.join(df_room, how = "inner")

# use set_index()
df_list.set_index("member").join(df_room.set_index("name"), how = "left")
df_list.set_index("member").join(df_room.set_index("name"), how = "inner")

# use reset_index()
df_list.set_index("member").join(df_room.set_index("name"), how = "left").reset_index()
df_list.set_index("member").join(df_room.set_index("name"), how = "inner").reset_index()
