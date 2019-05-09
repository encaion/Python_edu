import pandas as pd
import scipy.stats as sp
from matplotlib import pyplot as plt
df = pd.read_csv("AWS_sample.txt", sep = "#")
df = df.loc[df["AWS_ID"] == 108, :]
sp.probplot(df["TA"], plot=plt)
