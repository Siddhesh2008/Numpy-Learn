import numpy as np

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print("Array:\n", array)
print("Sum of all elements:", np.sum(array))
print("Sum along axis 0 (columns):", np.sum(array, axis=0))
print("Sum along axis 1 (rows):", np.sum(array, axis=1))
print("Mean of all elements:", np.mean(array))
print("Mean along axis 0 (columns):", np.mean(array, axis=0))
print("Mean along axis 1 (rows):", np.mean(array, axis=1))
print("Standard deviation of all elements:", np.std(array))
print("Standard deviation along axis 0 (columns):", np.std(array, axis=0))
print("Standard deviation along axis 1 (rows):", np.std(array, axis=1))
print("Minimum value of all elements:", np.min(array))
print("Minimum value along axis 0 (columns):", np.min(array, axis=0))
print("Minimum value along axis 1 (rows):", np.min(array, axis=1))
print("Maximum value of all elements:", np.max(array))
print("Maximum value along axis 0 (columns):", np.max(array, axis=0))
print("Maximum value along axis 1 (rows):", np.max(array, axis=1))
print("Variance of all elements:", np.var(array))
print("Variance along axis 0 (columns):", np.var(array, axis=0))
print("Variance along axis 1 (rows):", np.var(array, axis=1))
print("Cumulative sum of all elements:", np.cumsum(array))
print("Index of maximum value:", np.argmax(array))
print("Index of minimum value:", np.argmin(array))










