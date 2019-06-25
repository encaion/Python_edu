import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                  index = pd.date_range('1/1/2020', periods = 10))
df.iloc[3:7] = np.nan

df.agg(['sum', 'min'])

df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
