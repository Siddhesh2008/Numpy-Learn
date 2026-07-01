import numpy as np

ages=np.array([[25, 30, 35,20,67,30, 45, 50],
               [40, 45, 50, 55, 60, 65, 70, 75]])

teenagers = ages[ages<40]
oldppl=ages[ages>=40]     #can be used with &&,||,! logical operators as well.
eves=ages[ages%2==0]  #even numbers
print("Teenagers:\n", teenagers)
print("Adults:\n", oldppl)
print("Even numbers:\n", eves)

adukts=np.where(ages>=40, ages, 0)  #if condition is true then return ages else return 0
print("Adults:\n", adukts)