import pandas as pd
df = pd.read_csv("file.csv")
df.to_csv("test_gzip.gz", compression = "gzip", index = False)
# compression: 
# - Valid compression types are ['infer', None, 'bz2', 'gzip', 'xz', 'zip']

df = pd.read_csv("test_gzip.gz")
df.head()
