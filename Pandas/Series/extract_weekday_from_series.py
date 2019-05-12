import pandas as pd

df = pd.DataFrame({'date': ['2020-01-01', '2020-01-02', '2020-01-03'],
                   'value': [1, 2, 3]})
df['date'] = pd.to_datetime(df['date'])
df['date'].dt.day_name()
df['date'].dt.dayofweek
