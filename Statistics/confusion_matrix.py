import sklearn.metrics as skm
aa = [1, 1, 0, 0, 1, 1, 1]
bb = [0, 1, 0, 0, 1, 0, 1]

skm.confusion_matrix(aa, bb)
skm.accuracy_score(aa, bb)
skm.recall_score(aa, bb)
skm.precision_score(aa, bb)

from sklearn.metrics import classification_report
print(classification_report(aa, bb, target_names=['class 0', 'class 1']))


