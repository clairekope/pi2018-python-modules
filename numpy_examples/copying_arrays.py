# The importance of copying arrays

# This is a very short example. Copying arrays is expensive, but sometimes it is necessary.
 
# For example, let our original array be `a`:
a = np.arange(5)
# We want to copy and modify `a` without changing the original.


# The wrong way
b = a
print("a:", a)
print("b:", b)

b[0] = 5

print("a:", a)
print("b:", b)


# The right way
[0] = 0 # reset a
b = a.copy()
print("a:", a)
print("b:", b)

b[0] = 5

print("a:", a)
print("b:", b)

