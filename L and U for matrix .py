######TRY IT! Get the L and U for the above matrix A.

import numpy as np
from scipy.linalg import lu
a = np.array([[4, 3, -5],[-2,-4,5],[8,8,0]])

p,l,u=lu(a)
print(p)
print(l)
print(u)
print(np.dot(l,u))
######TRY IT! Multiply P and A and see what is the effect of the permutation matrix on A.
print(np.dot(p,a))