# # Getting statistical information from arrays

# There are many functions in NumPy that respond the same way to function arguments:
# - `np.sum` adds array elements
# - `np.prod` multiplies array elements
# - `np.mean` calculates the arithmetic mean
# - `np.average` can gives you a weighted average. If no weights are supplied, which is the default, it behaves just like np.mean
# - `np.median` calculates the median
# - `np.std` gives the standard deviation
# - `np.var` calculates the variance
# 
# We will introduce their behavior using `np.sum`.

# Make some data
data_2D = np.arange(9).reshape(3,3)
print(data_2D)

data_3D = np.arange(12).reshape(2,2,3)
print(data_3D)


# With no additional arguments:
print(np.sum(data_2D))

print(np.sum(data_3D))


# Specifying an axis:

# 2D

# Sum along Columns
print(np.sum(data_2D, 0))

# Sum along Rows
print(np.sum(data_2D, 1))

# 3D

# Sum all Slabs
print(np.sum(data_3D, 0))

# Sum along columns, so each 2D slab becomes a 1D array
print(np.sum(data_3D, 1))

# Ditto but with rows
print(np.sum(data_3D, 2))


# Trying the other functions

# Scramble the array of numbers from 0-9
test_2D = np.arange(9)
np.random.shuffle(test_2D)
test_2D = np.reshape(test_2D, (3,3))
print(test_2D)

test_3D = np.arange(12)
np.random.shuffle(test_3D)
test_3D = np.reshape(test_3D, (2,2,3))
print(test_3D)

print(np.mean(test_2D))

print(np.mean(test_2D,0))

print(np.std(test_2D,0))

print(np.mean(test_3D,0))


# Now you try it
# Play around with both 2D and 3D data
