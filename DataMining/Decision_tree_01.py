import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix  
from sklearn.model_selection import train_test_split 

df = pd.read_csv("classification_data_01.csv")
X = df.drop("Class", axis=1)  
y = df["Class"]  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  
clf = tree.DecisionTreeClassifier()  
clf.fit(X_train, y_train)  
y_pred = clf.predict(X_test)  

confusion_matrix(y_test, y_pred)
clf.score(X_train, y_train)
clf.score(X_test, y_test)
