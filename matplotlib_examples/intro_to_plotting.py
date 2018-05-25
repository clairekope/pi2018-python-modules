# Introduction to Plotting with Matplotlib

# See the Matplotlib section of this morning's Google doc 
# (https://docs.google.com/document/d/1_2_IhFYTBnNWIKik4M2GqbaY3i78IJDD9-6J4A3bNNI/edit?usp=sharing)
# or the Matplotlib Usage Guide 
# (https://matplotlib.org/tutorials/introductory/usage.html)
# for an introduction to Matplotlib terminology.

# **Disclaimer:** Matplotlib works differently in Jupyter notebooks than in scripts. I have done my best to make both formats behave as consistently as possible.

import numpy as np
import matplotlib; matplotlib.use('agg') # no gui
import matplotlib.pyplot as plt
# turn off interactive plotting


# We can use the `subplots` function to create both a Figure and Axes within the figure.
 
# `subplots` will arrange your axes in rows and columns. 
# Below, we ask for two rows and one column, and also ask that the x axis be 
# shared among all Axes.
fig, ax = plt.subplots(2,1,sharex=True)
# The boxes are our Axes objects, and they live within the Figure object.


# Because we've asked `subplots` for multiple axes, the `ax` variable will be a list of Axes objects.
print(ax)


# Let's plot both $\sin x$ and $\cos x$ from $0$ to $2\pi$.
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax[0].plot(x,y1)
ax[1].plot(x,y2)

# since our session isn't interactive:
plt.show()

# to save our figure:
fig.savefig('first_plot.png')


# Improving Plots
# We can manipulate our plots in several ways, demonstrated below. 


# Adding axis labels
ax[0].set_ylabel('y')
ax[1].set_ylabel('y')

# Because we've chosen to share our x axes, we only need to label the bottom 
# x axis, which is the last in the list.
ax[1].set_xlabel('x')


# Setting axis limits
ax[1].set_ylim(-1,0)

# Because we've chosen to share our x axes, both x axes will update simultaneously.
ax[0].set_xlim(1,5)


# Adding a title to the axis
ax[0].set_title('Sine')
ax[1].set_title('Cosine')


# Adding a title to the figure
fig.suptitle('Line Plots')


# Including a grid
ax[0].grid()


# Adding a legend
ax[1].legend(['cos(x)'])

# It's hard to get the plot to re-show, so let's just save to file
fig.savefig('modified_plot.png')

# Controlling the appearance of our lines

# Matplotlib has a default list of colors it will cycle through when we add 
# lines to the same Axes; however, we can control the appearance ourselves.
# This is done using several optional keywords:
# - `linestyle` or `ls` can be written with words
#   (`solid`, `dashed`, `dashdot`, `dotted`, `none`)
#   or symbols (`'-'`,`'--'`,`':'`, `' '` or `''`)
# - `linewidth` or `lw` is a float
# - `color` is a name like “purple”, or for common colors, just “b” for blue 
#   (“common” meaning RBG/CMYK colors)
# - `marker` is one of Matplotlib's many markers 
#   (https://matplotlib.org/api/markers_api.html#module-matplotlib.markers).
#   By default, no markers are used for `plot`
# 
# There is also the `label` object, which makes making legends easier.
# 
# Let's create a new Figure and a single Axes objects to play with these options:
fig, ax = plt.subplots()


# With only one Axes object on our Figure, `ax` is no longer a list.
ax.plot(x,y1, color='m', marker='.', label="sine")
ax.plot(x,y2, ls='--', lw=2, label='cosine')
ax.legend()

plt.show()
fig.savefig("line_options.png")
