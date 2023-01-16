
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

np.savez("diabetes.npz", X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)