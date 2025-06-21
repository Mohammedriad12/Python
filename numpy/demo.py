import numpy as np
# identity
arr = np.identity((5))
print(arr)

#full
arr  = np.full((2,3),4)
print (arr)

#full_like
ar = np.full_like(arr,1)
print(ar)

#random
arr = np.random.rand(2,3)
print(arr)

#repeat 
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)

#copy 
acopy = arr.copy()
print(acopy)