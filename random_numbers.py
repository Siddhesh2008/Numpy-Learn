import numpy as np

rng=np.random.default_rng(seed=1)  # Create a random number generator
print(rng.integers(1,7))
print(rng.integers(1,7, size=10))  # Generate an array of 10 random integers between 1 and 6

print(rng.random())  # Generate a random float between 0 and 1
print(rng.integers(1,101,size=(5,5)))  # Generate a 5x5 array of random integers between 1 and 100

print(np.random.uniform(0, 1, size=4))  # Generate an array of 4 random floats between 0 and 1


array=np.array([[1,2,3],[4,5,6],[7,8,9]])
rng.shuffle(array)  # Shuffle the array in place
print(array)  # Print the shuffled array
fruits=np.array(['apple','banana','cherry','date'])
fruits=rng.choice(fruits,size=(3,2))
print(fruits)  # Print a randomly selected fruit from the array
