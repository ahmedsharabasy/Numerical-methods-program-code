#TRY IT! Plot the vector x = [[1], [1]] and the vector b = Ax where A = [[2, 0], [0, 1]]

from cProfile import label
from turtle import color
from matplotlib import scale
import numpy as np
import matplotlib.pyplot as plt

# Ax=y
# Ax=b 
a=np.array([[2, 0], [0, 1]])
x=np.array([[1], [1]])
b=np.dot(a,x)

def plot_vector(x,y,xlim,ylim):
    plt.figure(figsize=(10,6))
    plt.quiver(0,0,x[0],x[1],color="k",angles="xy",scale_units='xy',scale=1,label="original vector")
    plt.quiver(0,0,y[0],y[1],color="g",angles="xy",scale_units="xy",scale=1,label="transformed vector")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

plot_vector(x,b,(0,3),(0,3))    
