#TRY IT! Use the qr function in numpy.linalg to decompose matrix A = ([[0, 2],[2, 3]])
#. Verify the results.

# import numpy as np
# from numpy.linalg import qr

# a = np.array([[0, 2],[2, 3]])

# q,r=qr(a)

# print(q)
# print(r)
# print(np.dot (q,r))

#TRY IT! Use the QR method to get the eigenvalues of matrix A =([[0, 2], [2, 3]])
#. Do 20 iterations, and print out the first, fifth, 10th, and 20th iteration.
import numpy as np
from numpy.linalg import qr
a = np.array([[0, 2],[2, 3]])
p=[1,5,10,20]
for i in range(20):
    q,r=qr(a)
    a=np.dot(r,q)
    if i+1 in p:
        print('iteration:',i+1)
        print('*********')
        print(a) 
        print(q)
        print(r)

