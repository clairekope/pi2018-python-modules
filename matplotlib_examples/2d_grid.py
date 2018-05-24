# Plotting fields on a 2D grid

import numpy as np
# use default backend
import matplotlib.pyplot as plt
# turn off interactive plotting


# If we define an arrays for our x and y points, with 50 points each
x = np.linspace(10,20,50)
y = np.linspace(0,10)


# The NumPy `meshgrid` function will create (x,y) pairs we can use in 2D functions:
xx, yy = np.meshgrid(x, y)
z = np.sin(xx) * np.sqrt(yy)


# A good way to view `z` is to use the `pcolormesh` function.
# One option is to pass just z:
fig, ax = plt.subplots()
ax.pcolormesh(z)

# since our session isn't interactive:
plt.show()

# to save our figure
fig.savefig('z_field.png')

# Notice that the x and y axes go from 0 to 50, instead of 10 to 20 and 0 to 10 like we specified above. That's because `pcolormesh` wasn't given any information about the x-y grid, and defaulted to using the shape of `z` (which is (50,50)).


 
# So now, let's also tell `pcolormesh` about the grid `z` is on:
fig, ax = plt.subplots()
ax.pcolormesh(x,y,z)

plt.show()
fig.savefig('z_grid.png')

