import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("diamonds.csv")

plt.hist(df.price, bins = 20, alpha = 0.3)
plt.hist(df.price, bins = 40, alpha = 0.3)
plt.hist(df.price, bins = 60, alpha = 0.3)
plt.close()
