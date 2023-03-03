#TRY IT! Calculate the eigenvalues and eigenvectors for matrix A = ([[0, 2],[2, 3]])

import numpy as np
from numpy.linalg import eig
a = np.array([[0, 2],[2, 3]])
w,v=eig(a)
print("E-value:", w)
print("E-vector", v)