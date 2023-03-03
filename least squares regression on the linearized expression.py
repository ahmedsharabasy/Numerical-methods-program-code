# '''Assume you have a function in the form ˆ y(x) = αeβx and data for x and y, and that you want to
# perform least squares regression to find α and β. Clearly, the previous set of basis functions (linear)
# would be inappropriate to describe ˆ y(x); however, if we take the log of both sides, we get log( ˆ y(x)) =
# log(α) +βx. Now, we see that if ˜ y(x) = log( ˆ y(x)) and ˜α = log(α), then ˜ y(x)= ˜α + βx. Thus, we can
# perform a least squares regression on the linearized expression to find ˜ y(x), ˜α , and β, and then recover
# α by using the expression α = e
# ˜α
# .
# For the example below, we will generate data using α = 0.1 and β = 0.3.'''

from operator import le
from tkinter.messagebox import NO
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

x=np.linspace(0,10,101)
y=.1*np.exp(.3*x)+.1*np.random.random(len(x))
A=np.vstack([x,np.ones(len(x))]).T
beta,log_alpha=np.linalg.lstsq(A,np.log(y),rcond=None)[0]
alpha=np.exp(log_alpha)
print(f'alpha{alpha},beta{beta}')

plt.figure(figsize=(10,8))
plt.plot(x,y,"k")
plt.plot(x,alpha*np.exp(beta*x),"r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

