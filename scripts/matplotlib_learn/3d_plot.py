import matplotlib.pyplot as plt
import numpy as np

# create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# generate meshgrid data for x, y, and calculate z
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax.set_title('3D Surface Plot')
plt.show()
