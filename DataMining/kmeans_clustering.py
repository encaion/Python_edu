from sklearn.metrics import confusion_matrix  
from sklearn.cluster import KMeans
import pandas as pd
df = pd.read_excel("iris_xlsx.xlsx")
df.head()

X = df.loc[:, :"Petal.Width"]

kmeans = KMeans(n_clusters=3)
kmeans = kmeans.fit(X)

centroids = pd.DataFrame(kmeans.cluster_centers_, columns = X.columns)
centroids

df["cluster"] = kmeans.predict(X)
df["cluster"] = df["cluster"].replace({1: "setosa", 0: "versicolor", 2: "virginica"})
confusion_matrix(df["Species"], df["cluster"])
