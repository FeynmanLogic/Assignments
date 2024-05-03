import numpy as np
X=np.array([12,34,45,21])
Y=np.array([1,3,4,0])
Z=np.dot(X,Y)
print(Z)
print(X.ndim)
arr=np.concatenate((X,Y))
print(arr)
