# solving system of linear equation
#####1

# '''
# TRY IT! Use numpy.linalg.solve to solve the following equations:
# 4x1 +3x2 −5x3 = 2,
# −2x1 −4x2 +5x3 = 5,
# 8x1 +8x2 = −3.
# '''

import numpy as np
from numpy.linalg import solve

a=np.array([[4,3,-5],[-2,-4,5],[8,8,0]])
y=np.array([2,5,3])
c=np.linalg.solve(a,y)
print(c)


