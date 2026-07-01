import numpy as np

#scalar arithmetic operations nad vector operations
a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)     #can be done separetly also for  array with a integer

print(np.sqrt(a))     #some vector functions
print(np.exp(a))
print(np.log(a))
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
#can be rounded also
print (a**2)     #some scalar functions
print (a%2)
print (a//2)

##comparison operations

scores = np.array([10,20,30,40,50])

print(scores>30)    # gives boolean
print(scores<30)
print(scores>=30)
print(scores<=30)
print(scores==30)
print(scores!=30)