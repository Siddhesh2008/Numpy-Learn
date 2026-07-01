##We use array_split() for splitting arrays, we pass it the array
# we want to split and the number of splits.


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
##If the array has less elements than required, it will adjust from the end accordingly.

#Access the splitted arrays:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

##Split the 2-D array into three 2-D arrays.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)        #hsplit=horizontal split
                   #vsplit=vertical split
                    #dsplit=depth split