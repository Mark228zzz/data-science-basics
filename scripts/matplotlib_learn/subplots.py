import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) # create data

# create a figure with two vertically stacked subplots
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# plot sin(x) on the first subplot
ax[0].plot(x, np.sin(x), label='sin(x)', color='blue')
ax[0].set_title('Sin(x)')
ax[0].legend()

# plot cos(x) on the second subplot
ax[1].plot(x, np.cos(x), label='cos(x)', color='green')
ax[1].set_title('Cos(x)')
ax[1].legend()

# adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
