import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)    #if the elements required are present in the array, 
                  #it will return the array with the new shape
                  
                  
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)       #to flatten an multidimensional array, we can pass -1
#                               as the new shape.

print(newarr)         #any one axis can be -1 as unknown value, and NumPy will calculate this number for you.