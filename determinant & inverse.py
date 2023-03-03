#The inverse of a square matrix M is a matrix of the same size, N, such that M · N = I
#TRY IT! 
#The matrix M (in the previous example) has a nonzero determinant. Compute the inverse
#of M. Show that the matrix P = [[0, 1, 0], [0, 0, 0], [1, 0, 1]] has a determinant value of zero, and
#therefore has no inverse.

import numpy as np
from numpy.linalg import det
from numpy.linalg import inv
M = np.array([[0,2,1,3],[3,2,8,1],[1,0,0,3],[0,3,2,1]])
print(inv(M))

P = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]
print(det(P))
if det(P)==0:
    print("has no inverse")
else:    
    print('has inverse')    

