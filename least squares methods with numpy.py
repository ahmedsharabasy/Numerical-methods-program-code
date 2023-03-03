# '''USING NUMPY.LINALG.LSTSQ
# NumPy has already implemented the least squares methods, so we can just call the function to get a
# solution. The function will return more data than the solution itself; please check the documentation
# for details.
# '''

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 101)
print(x)
y = 1 + x + x * np.random.random(len(x))
print(y)

y=y[:,np.newaxis]

A = np.vstack([x, np.ones(len(x))]).T

alpha=np.linalg.lstsq(A,y,rcond=None)[0]
print(alpha)

plt.figure(figsize=(10,6))
plt.plot(x,y,"b")
plt.plot(x,alpha[0]*x+alpha[1],"r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()