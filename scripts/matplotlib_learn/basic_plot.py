import matplotlib.pyplot as plt
import numpy as np

# create a data
x = np.linspace(0, 10, 100) # make random data
y = np.sin(x)

# basic of plotting
plt.plot(x, y, label='y=sin(x)') # plot the graph
plt.title('Basic Plot') # the name of plot at the top
plt.xlabel('x-axis') # the name of x-axis
plt.ylabel('y-axis') # the name of y-axis
plt.legend() # draw the labels at the right top
plt.show() # show the plot
