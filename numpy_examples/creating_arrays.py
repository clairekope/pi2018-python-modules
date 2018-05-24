# Common ways of creating arrays

import numpy as np

# From existing data
data_1D = np.array([7.21,80,9.5,3,11,93.7])
print(data_1D)

data_2D = np.array([ [5,6.8,9], [10,3,4.5], [8.1,2,13] ])
print(data_2D)

data_3D = np.array( [[[1,2,3],[4,5,6]], [[1.2,5.3,8],[9.1,3,6]]] )
print(data_3D)


# All ones or zeros

ones_1D = np.ones(15)
print(ones_1D)

zeros_3D = np.zeros( (3,3,3) )
print(zeros_3D)


# Array of random numbers

# Sample a uniform distribution between 0 and 1
print(np.random.rand(3,3))

# Sample the standard normal distribution
print(np.random.randn(3,3))


# Using `arange` and `linspace`

# `np.arange` can take 1, 2, or 3 arguments
print(np.arange(10))

print(np.arange(5,10))

print(np.arange(1,10,3))

# We can also count backwards:
print(np.arange(10,1,-3))


# `np.linspace` must take at least 2 arguments, but will also accept a third.
l = np.linspace(10,20)
print(l)
print("Size:", l.size)

l = np.linspace(10,20,30)
print(l)
print("Size:", l.size)

# `linspace` will also run backwards:
print(np.linspace(20,10,30))

