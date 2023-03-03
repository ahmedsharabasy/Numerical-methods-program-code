# '''USING OPTIMIZE.CURVE_FIT FROM SCIPY
# This SciPy function is very powerful. It is not only suitable for linear functions, but many different
# function forms as well, such as nonlinear functions. Here we will only show the linear example from
# above. Note that, when using this function, we do not need to turn y into a column vector.'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
plt.style.use("seaborn-poster")

x = np.linspace(0, 1, 101)
print(x)
y = 1 + x + x * np.random.random(len(x))
print(y)

# def fit(x,a,b):
#     y=a*x+b
#     return y

# alpha= optimize.curve_fit(fit,xdata=x,ydata=y)[0]
# print(alpha)    
def func(x, a, b):
    y = a*x + b
    return y

alpha=optimize.curve_fit(func, xdata=x, ydata=y)[0]
print(alpha)
