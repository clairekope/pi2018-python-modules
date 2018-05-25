# Plotting lines & scatter plots with error bars

import numpy as np
import matplotlib; matplotlib.use('agg') # no gui
import matplotlib.pyplot as plt
# turn off interactive plotting


# First, let's generate data for a line plot with a constant relative error of 10%.
x1 = np.linspace(0,10)
y1 = np.sqrt(x1)
dy1 = 0.1*y1


# Next, we'll use `np.genfromtxt` to load `"sample_data.txt"`, which contains measurements for the distribution of flowers in a field. The uncertainties in the x and y positions are saved to `dx` and `dy`.
x2, dx2, y2, dy2, count = np.genfromtxt("sample_data.txt", skip_header=2,
                                        delimiter=',', unpack=True)

# Both line and scatter plots can be plotted with error bars using the `errorbar` function. To make a scatter plot, we must set the linestyle to `'none'` and pick a marker.
fig, ax = plt.subplots(1,2)
ax[0].errorbar(x1, y1, yerr=dy1)
ax[1].errorbar(x2, y2, xerr=dx2, yerr=dy2, ls='none', marker='.')

# since our session isn't interactive:
plt.show()

# to save our figure:
fig.savefig("error_bar.png")
