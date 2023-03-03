# 1-A matrix that is close to being singular (i.e., the determinant is close to zero) is called ill-conditioned
# 2-The condition number is a measure of how ill-conditioned a matrix is:
# 3-The higher the condition number, the closer the matrix to being singular.
 
# TRY IT! For the matrix A = [[1, 1, 0], [0, 1, 0], [1, 0, 1]], compute the condition number

import numpy as np
from numpy.linalg import cond
A = np.array([[1, 1, 0], [0, 1, 0], [1, 0, 1]])
print(cond(A))

