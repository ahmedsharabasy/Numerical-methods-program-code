#TRY IT! Implement the power method in Python

# import numpy as np

# def normalize(x):
#     Max=abs(x).max()
#     x_new=x/x.max()
#     return Max,x_new
    

# a=np.array([[0,2],[2,3]])
# x=np.array([1,1])    


# for i in range(8):
#     x=np.dot(a,x)
#     y,x=normalize(x) 

# print("eigen value",y)
# print("eifen vector",x)


#smallest eigen (sallest power m)
import numpy as np
from numpy.linalg import inv

def normalize(x):
    Max=abs(x).max()
    x_new=x/x.max()
    return Max,x_new
    

a=np.array([[0,2],[2,3]])
x=np.array([1,1])    
a_inv=inv(a)

for i in range(8):
    x=np.dot(a_inv,x)
    y,x=normalize(x) 

print("eigen value",y)
print("eifen vector",x)
