import numpy as np

arrays =np.array([['a','b','c'],
                ['d','e','f'],
                ['g','h','i']])
print(arrays.ndim)   #number of dimensions
print(arrays.shape)  #number of rows and columns
print(arrays[0,2])      #first row and third column

word=arrays[0,2]+arrays[1,2]+arrays[2,2]
print(word)    #concatenation