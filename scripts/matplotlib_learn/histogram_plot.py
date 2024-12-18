import matplotlib.pyplot as plt
import numpy as np

# generate random data from a normal distribution
data = np.random.randn(2000)

# create a histogram with 30 bins
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
