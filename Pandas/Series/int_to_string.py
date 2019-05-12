import pandas as pd
ser = pd.Series([1, 2, 3])
ser = ser.astype("str")
ser[3] = "asdf"
print(ser)
