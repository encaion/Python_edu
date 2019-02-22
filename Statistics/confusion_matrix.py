from sklearn.metrics import confusion_matrix  
from sklearn.metrics import classification_report
aa = [1, 1, 0, 0, 1, 1, 1]
bb = [0, 1, 0, 0, 1, 0, 1]

confusion_matrix(aa, bb)
print(classification_report(aa, bb, target_names=['class 0', 'class 1']))

accuracy_score(aa, bb)
precision_score(aa, bb)
recall_score(bb, bb)
