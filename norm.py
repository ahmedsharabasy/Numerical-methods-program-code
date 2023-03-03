#calc norm (distance)

import numpy as np
from numpy.linalg import norm
vector_row=np.array([[1,5,5,8,10]])
new_vec=vector_row.T
print(new_vec)

norm1=norm(new_vec,1)
norm2=norm(new_vec,2)
norm_inf=norm(new_vec,np.inf)

print('L1= %.1f'%norm1)
print('L1=%.1f'%norm2)
print('L1=%.1f'%norm_inf)