##to search an array, use the where() method.


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)       #returns the indices of the elements that are equal to 4

print(x)

##Find the indexes where the value 7 should be inserted:
#There is a method called searchsorted() which performs a binary search in the array, and returns the index where 
#the specified value would be inserted to maintain the search order.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)