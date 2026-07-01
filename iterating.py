import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
  
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)  #iterates as 1, 2, 3, 4, 5, 6
    

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)       ##using nditter removes extra loops and iterates through all the elements of the array,
                  #no matter how many dimensions it has.
                  
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)        #The flags=['buffered'] allows the iteration to use a temporary buffer, and op_dtypes=['S'] specifies that the output data type should be string. This means that each element of the array will be converted to a string during iteration.



##Iterate through every scalar element of the 2D array skipping 1 element:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)
  


#Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
#Enumerate on following 1D arrays elements:

import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)