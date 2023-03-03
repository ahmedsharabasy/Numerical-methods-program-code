#Find the determinant of matrix M = [[0, 2, 1, 3], [3, 2, 8, 1], [1, 0, 0, 3], [0, 3, 2, 1]]. Use the
#np.eye function to produce a 4×4 identity matrix, I . Multiply M by I to show that the result is M.

import numpy as np
from numpy.linalg import det
M = np.array([[0,2,1,3],
[3,2,8,1],
[1,0,0,3],
[0,3,2,1]])

print('determinant:  ',det(M))

I=np.eye(4)
print('I:  ',I)
print('*'*30)
print('M*I:  ',np.dot(M,I))
