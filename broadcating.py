from re import match

import numpy as np

# Example of broadcasting: add a 1D array to a 2D array
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
vector = np.array([1, 2, 3])

# The vector is broadcast across each row of the matrix
result = matrix + vector

print("Matrix:\n", matrix)
print("Vector:\n", vector)
print("Result after broadcasting:\n", result)
##like matrice multiplication

#should have either 1 or both row or column should match for broadcasting to work.
# In this case, the vector has 3 elements, which matches the number 
# of columns in the matrix, allowing it to be added to each row of the matrix

#for example, if we had a 2D array with shape (3, 1) and a 1D array with shape (3,), 
# we could also broadcast them together. The 1D array would be treated 
# as a column vector and added to each row of the 2D array.

array1=np.array([[1,2,3,4,5,6,7,8,9,10]]) #shape (1, 10)
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]) #shape (10, 1)

print(array1*array2)