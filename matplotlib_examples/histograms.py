# Plotting Histograms

import numpy as np
import matplotlib; matplotlib.use('agg') # no gui
import matplotlib.pyplot as plt
# turn off interactive plotting


# Use `np.genfromtxt` to load `"sample_data.txt"`, which contains measurements for the distribution of flowers in a field.
x, dx, y, dy, count = np.genfromtxt("sample_data.txt", skip_header=2,
                                    delimiter=',', unpack=True)


# To create a histogram, we have to supply the numbers we want to bin and, optionally, the number of bins. 
# 
# The `hist` call will return the number of objects per bin and an array of bin edges, in addition to the plot object. This makes it different from other plot types, which only return the plot object.

fig, ax = plt.subplots()
num, edges, p = ax.hist(count, 20)

# since our session isn't interactive:
plt.show()

# to save our figure:
fig.savefig('hist.png')

print(num)
print(edges)
