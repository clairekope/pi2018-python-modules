# Explore the utility of boolean arrays

import numpy as np

# Create a 2D array we can play with
data_1D = np.arange(12)
data_2D = data_1D.reshape((3,4))
print(data_2D)

# Which elements are even numbers?
is_even = data_2D%2 == 0
print(is_even)

# Extract the even elements
even_elements = data_2D[is_even]
print(even_elements)

# Now you try:
# Can you extract elements divisible by 3?
is_divisible = 
divisible_elements = 
print(divisible_elements)
