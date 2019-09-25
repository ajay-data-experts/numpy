#get the package - for scientific computing
#high performance multidimensional array
#Memory efficiency
#easy to use - no need to use loop
#Fast - take less time
import numpy as np


#1. Single dimension array
a = np.array([1,2,3,4])
print(a)

#2. 2-Dimensional array
b = np.array([(1,2,3,4),(5,6,7,8)])
print(b)

#Operations
#1. Dimensions

b = np.array([(1,2,3,4),(5,6,7,8)])
print(b.ndim)

print('1 dimension')
b = np.array([1,2,3,4])
print(b.ndim)
