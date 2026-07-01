import numpy as np

#We pass a sequence of arrays that we want to join to the concatenate() function,
# along with the axis. If axis is not explicitly passed, it is taken as 0.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

##We pass a sequence of arrays that we want to join to the stack() method along with the axis.
# If axis is not explicitly passed it is taken as 0.
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)   #output: [[1 4]
                                       #         [2 5]
                                       #         [3 6]] #vstack=vertical stack
                                       #                #dstack=depth stack
                                       #        #hstack=horizontal stack

print(arr)