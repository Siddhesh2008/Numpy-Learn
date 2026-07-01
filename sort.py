##The NumPy ndarray object has a function called sort(),
# that will sort a specified array.defaullt=ascending order.


import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

##Sort a 2-D array:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))   ##output: [[2 3 4]
                      #         [0 1 5]] #sorts each row in ascending order
                      
#for descending order, we can use the sort() method of ndarray object.

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr)[::-1])