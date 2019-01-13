import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

truelbls=[2,0,0,2,4,4,1,0,3,3,3]
predlbls=[2,1,0,2,4,3,1,0,1,3,3]

confusion_mat=confusion_matrix(truelbls, predlbls)

plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.gray)
plt.title('confusion matrix')
plt.colorbar()
ticks=np.arange(5)
plt.xticks(ticks,ticks)
plt.yticks(ticks,ticks)
plt.xlabel('True labels')
plt.ylabel('Predicted labels')
plt.show()

targets=['Class-0','Class-1','Class-2','Class-3','Class-4']
print(classification_report(truelbls, predlbls, target_names=targets))
