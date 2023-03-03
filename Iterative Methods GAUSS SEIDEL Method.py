# Iterative Methods GAUSS SEIDEL Method
# '''
#    EXAMPLE: Solve the following system of linear equations using Gauss–Seidel method using a
#   predefined threshold machine epsilon= 0.01. Remember to check if the converge condition is satisfied or not.
#   8x1 +3x2 −3x3 = 14,
#   −2x1 −8x2 +5x3 = 5,
#   3x1 + 5x2 +10x3 = −8.
# '''
from pickle import TRUE
from this import d
from matplotlib.pyplot import axis
import numpy as np

a=np.array([[8,3,-3],[-2,-8,5],[3,5,10]])

diag=np.diag(np.abs(a))                     #np.diag
off_diag = np.sum(np.abs(a),axis=1)-diag    #np.sum

if np.all(diag>off_diag):
    print("M is diagonally dominant")
else:
    print("M is not diagonally dominant")    

x1=0
x2=0
x3=0
epsilon=.01
converged=False
x_old=np.array([x1,x2,x3])
print("   iteeation result")
print("K,   x1,   x2,    x3")

for k in range(1,50):
    x1=(14-3*x2+3*x3)/8
    x2=(5+2*x1-5*x3)/(-8)
    x3=(-8-3*x1-5*x2)/(10)

    x=np.array([x1,x2,x3])

    dx=np.sqrt(np.dot(x-x_old,x-x_old))
    print("%d,%.4f,%.4f,%.4f"%(k,x1,x2,x3))

    if dx<epsilon:
        converged=TRUE
        print("converged")
        break
    x_old=x    #مينفعش العكس


if not converged:
    print("not converged, icrease number of iterations")




