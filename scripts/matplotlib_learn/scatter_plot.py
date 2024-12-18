import matplotlib.pyplot as plt
import numpy as np

# generate random data points for scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 100  # random sizes for the points
colors = np.random.rand(50)  # random colors for the points

# create a scatter plot with color map and transparency
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.6, edgecolors='w')
plt.title('Scatter Plot')
plt.colorbar(label='Color Scale')  # add a color scale
plt.show()
