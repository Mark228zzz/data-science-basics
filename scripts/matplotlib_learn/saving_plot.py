import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.tanh(x)

# create a simple plot and save it as a PNG file
plt.plot(x, y, label='Example')
plt.title('Saving Figure Example')
plt.legend()
plt.savefig('./scripts/matplotlib_learn/saves/example_plot.png', dpi=300)  # save with specified resolution
plt.close()  # close the figure to free memory
