import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import plt
df = pd.read_csv("AWS_sample.txt", sep = "#")
df = df.loc[df["AWS_ID"] == 108, :]
df['TM'] = pd.to_datetime(df['TM'])
# df.reset_index(inplace=True)
df = df.set_index("TM")
df.head(2)

series = df["TA"]
result = seasonal_decompose(series, model='additive')
result.plot()
