import numpy as np

x0=np.ones(10)
x1=np.array(range(10))
x2=x1**2
x3=x1**3
y=np.array([1,3,4,7,9,11,15,18,20,25])

X=np.array([x0,x1,x2,x3]).T

A=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y)

print(A)
