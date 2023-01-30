# random module provides functions that generate pseudorandom numbers

import random

# The seed() method is used to initialize the random number generator.

random.seed(42)

# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0). 
# The function randint returns a random int between high and low (including both). 
# (remember you must specify the function with a dot notation)
# This program produces the 2 list of 10 random numbers using random and randint

for i in range(10):
    x = random.random()
    print(x)
for j in range (10):
    y = random.randint(0, 10)
    print(y)

# To choose an element from a sequence at random, you can use choice:

t = [1, 2, 3]
print(random.choice(t))

# The random module also provides functions to generate random values from
# continuous distributions including Gaussian, exponential, gamma, and a few more.