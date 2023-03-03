#Let matrices P and Q be [[1, 7], [2, 3], [5, 0]] and [[2, 6, 3, 1], [1, 2, 3, 4]], respectively. Compute
#the Python matrix product of P and Q. Show that the product of Q and P will produce an
#error.
import numpy as np

P = np.array([[1, 7], [2, 3], [5, 0]])
Q = np.array([[2, 6, 3, 1], [1, 2, 3, 4]])
print(P)
print(Q)
print('*'*30)
print(np.dot(P, Q))
np.dot(Q, P)
