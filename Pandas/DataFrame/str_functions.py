import pandas as pd
df = pd.read_csv("diamonds.csv")
df = df.iloc[:8, :6]
df.head()

df["clarity"].str.len()
df["clarity"].str.match("VS1")
df["clarity"].str.lower()
df["clarity"].str.isupper()
df["clarity"].str.extract("([A-Z]{3,})")
df["clarity"].str.extract("(^[A-Z]{2}[0-9])")
df["clarity"].str.extract("([A-Z]{3,})").notnull()
df["clarity"].str.contains("([A-Z]{3,})")

#capitalize
#cat
#center
#contains
#count
#decode
#encode
#endswith
#extractall
#find
#findall
#get_dummies
#index
#isalnum
#isalpha
#isdecimal
#isdigit
#isnumeric
#isspace
#istitle
#islower
#isupper
#join
#len
#ljust
#lower
#lstrip
#match
#normalize
#pad
#partition
#repeat
#replace
#rfind
#rindex
#rjust
#rpartition
#rsplit
#rstrip
#slice
#slice_replace
#split
#startswith
#strip
#title
#translate
#upper
#wrap
#zfill
