# https://blog.shahinrostami.com/2018/09/jupyter-notebook-and-updating-plots/
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output

df = pd.read_csv("bosch_numeric_1_30.gz")

for n in np.r_[1:df.shape[1]]:
    df[df.columns[n]].hist(bins = 50, xlabelsize = 5)
    plt.title(df.columns[n])
    plt.xlabel("x axis")
    plt.ylabel("y axis", size = 20)
    plt.show()
    plt.pause(2)
    clear_output()
