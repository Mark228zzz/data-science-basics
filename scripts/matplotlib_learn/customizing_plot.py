import matplotlib.pyplot as plt
import numpy as np

# create a data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# customing plot
plt.style.use('dark_background')

plt.figure(figsize=(15, 8))
plt.plot(x, y, color='red', linestyle='--', linewidth=3, label='y=sin(x)', alpha=0.6)
plt.title('Customized Plot', fontsize=14)
plt.xlabel('x-axis', fontsize=12)
plt.ylabel('y-axis', fontsize=12)
plt.grid(True, linestyle='-.', alpha=0.1)
plt.legend()
plt.show()
