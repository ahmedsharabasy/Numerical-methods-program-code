# '''USING THE PSEUDO-INVERSE
# We mentioned earlier that the matrix (AT A)
# −1AT is called the pseudo-inverse, therefore, we can use
# the pinv function in NumPy to calculate it directly.'''
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 101)
print(x)
y = 1 + x + x * np.random.random(len(x))
print(y)

y=y[:,np.newaxis]

A = np.vstack([x, np.ones(len(x))]).T

pinv=np.linalg.pinv
alpha=pinv(A).dot(y)


print(alpha)
plt.figure(figsize=(10,6))
plt.plot(x,y,"b")
plt.plot(x,alpha[0]*x+alpha[1],"r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()