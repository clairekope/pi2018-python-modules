# Scatter Plots and Adding Colorbars

import numpy as np
# use default backend
import matplotlib.pyplot as plt
# turn off interactive plotting


# Use `np.genfromtxt` to load `"sample_data.txt"`, which contains measurements 
# for the distribution of flowers in a field.
x, dx, y, dy, count = np.genfromtxt("sample_data.txt", skip_header=2,
                                    delimiter=',', unpack=True)


# A simple scatter plot shows the distribution of (x,y) points.
fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

# since our session isn't interactive:
plt.show()
# to save our figure:
fig.savefig("scatter.png")


# Conveying Magnitude
# Our data contains more than just x and y. We also have information about the 
# number of flowers at each point. There are two ways we can convey this
# information through our scatter plot: size and color.

# Size
# We can use the size of the scatter plot markers to indicate the relative
# number of flowers at each location by passing `count` to the `s` argument
fig, ax = plt.subplots()
ax.scatter(x,y,s=count)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

plt.show()
fig.savefig("scatter_size.png")


# Color
# To color the scatter plot markers based on the number of flowers at that
# point, we must pass `count` to the `c` argument.
# If we're going to use color to convey information, we had better include a
# color bar. To create a color bar, we must save the plot object returned by
# `scatter` to a variable, so that the color bar knows what to scale to.
fig, ax = plt.subplots()
p = ax.scatter(x,y,c=count)
fig.colorbar(p)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

plt.show()
fig.savefig("scatter_color.png")

