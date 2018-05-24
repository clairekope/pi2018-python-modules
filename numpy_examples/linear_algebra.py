# Linear Algebra in NumPy

# Through a lot of these examples, we've been treating NumPy arrays as data containers.
# But we can also treat them like vectors and matrices.
# NumPy provides support for linear algebra operations both within NumPy
# and its sub-module `linalg`.

import numpy as np
import numpy.linalg as la


# First we make matrices and vectors to play with:
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4]])
M = np.array([[1,2],[3,4]]) # square matrix
a = np.array([4,5,6])
b = np.array([7,8,9])
v = np.array([5,6])


# ## Transpose

# We can transpose an array using `.T`:
print(A)
print(A.T)

# It has no affect on 1D arrays
print(a)
print(a.T)


# Multiplication

# The `np.dot` function (and its cousin, the `.dot` method) is very flexible and will combine any two `ndarray`s of any dimension. See [the documentation.](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html)

# Vector Dot Product

# Dot products should be commutative.
print(np.dot(a,b))
print(np.dot(b,a))

print(a.dot(b))
print(b.dot(a))


# Vector-Matrix Multiplication

# This operation is not commutative, just as we expect.
print(np.dot(A,a))
print(np.dot(a,A))

# When using the `.dot` method, the object to which the method belongs is on the left of the equation:
print(A.dot(a))


# Matrix-Matrix Multiplication

# Once again, this operation is not commutative, as we expect.
print(np.dot(B,A))
print(B.dot(A))
print(A.dot(B))

# The `dot` function is very general, and therefore slower at matrix multiplication than the specialized `matmul` function. 


# Solving Matrix Equations Mx=v
# Now we'll start using functions from the `linalg` module, which we imported as `la`.
x = la.solve(M,v)
print(x)

# Inverting Square Matrices
Minv = la.inv(M)
print(Minv.dot(M))
print(M.dot(Minv))

# Eigenvalues and Eigenvectors
evals, evecs = np.linalg.eig(M)
print(evals.shape)
print(evecs.shape)
# Each column of `evecs` corresponds to the eigevalues in `evals`.
vec = evecs[:,0]
print(M.dot(vec))
print(evals[0] * vec)


# Matrix Norms
# We can compute several different matrix norms. The default is the Frobenius 2-norm
la.norm(M)

# We could also specify the infinity-norm:
la.norm(M, ord=np.inf)

