import numpy as np
from sklearn import datasets
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle

data=datasets.load_boston()
X, y=shuffle(data.data, data.target, random_state=7)
numtrain=int(0.8*len(X))
X_train, y_train=X[:numtrain], y[:numtrain]
X_test, y_test=X[numtrain:], y[numtrain:]
sv_regressor=SVR(kernel='linear', C=1.0, epsilon=0.1)
sv_regressor.fit(X_train, y_train)

y_test_pred=sv_regressor.predict(X_test)
mse=mean_squared_error(y_test, y_test_pred)
evs=explained_variance_score(y_test, y_test_pred)

print("performance \n")
print("Mean squared error= ",round(mse,2))
print("Explained variance score ", round(evs,2))

