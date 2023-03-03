# '''TRY IT! Consider the artificial data created by x = np.linspace(0, 1, 101) and y = 1 + x
# + x * np.random.random(len(x)). Do a least squares regression with an estimation function
# defined by ˆy = α1x +α2. Plot the data points along with the least squares regression. Note that
# we expect α1 = 1.5 and α2 = 1.0 based on this data. Due to the random noise we added into the
# data, your results maybe slightly different.


import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

x = np.linspace(0, 1, 101)
print(x)
y = 1 + x + x * np.random.random(len(x))
print(y)
y=y[:,np.newaxis]
A=np.vstack([x,np.ones(len(x))]).T
print(A)
alpha= np.dot(np.dot(np.linalg.inv(np.dot(A.T,A)),A.T),y) #np.linallg.inv
print(alpha)

plt.figure(figsize=(10,6))
plt.plot(x,y,"b")
plt.plot(x,alpha[0]*x+alpha[1],"r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()