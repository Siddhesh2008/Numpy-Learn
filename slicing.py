import numpy as np

arrays=np.array([['a','b','c'],
    ['d','e','f'],
    ['g','h','i']])
#arrays[start:stop:step]
print(arrays[0:])  #all
print(arrays[0:3:2])  #first three rows with a step of 2
print(arrays[0:2,0:2])  #first two rows and first two columns
