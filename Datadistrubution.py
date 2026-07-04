#The probability for the value to be 3 is set to be 0.1

#The probability for the value to be 5 is set to be 0.3

#The probability for the value to be 7 is set to be 0.6

#The probability for the value to be 9 is set to be 0
#The choice() method allows us to specify the probability for each value.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)