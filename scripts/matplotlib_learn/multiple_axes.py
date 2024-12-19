import matplotlib.pyplot as plt
import numpy as np

# create two data series
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.exp(-x)

# create a figure with two y-axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # create a second y-axis sharing the same x-axis

# plot sin(x) on the first y-axis
ax1.plot(x, y1, 'g-', label='sin(x)')
ax2.plot(x, y2, 'b--', label='exp(-x)')  # plot exp(-x) on the second y-axis

# label axes with different colors
ax1.set_xlabel('x-axis')
ax1.set_ylabel('sin(x)', color='green')
ax2.set_ylabel('exp(-x)', color='blue')

# add legend and title
fig.legend(loc='upper right')
plt.title('Multiple Axes')
plt.show()
