import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("diamonds.csv")

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
fig

ax1.scatter(df.table, df.price)
fig

df_sub = df.loc[(df["cut"] == "Ideal"),:]
ax3.scatter(df_sub.table, df_sub.price, color = "#ffaacc")
fig
