import pandas as pd
ser = pd.Series(["1시간 3분", "15분", "23분"])
ser

ser.str.extractall("([0-9]{,2})시간 ([0-9]{,2})분|([0-9]{,2})분")
