import matplotlib.pyplot as plt
import numpy as np

# create a data
x = np.linspace(0, 10, 100) # make random data
y = np.sin(x)

# basic of plotting
plt.plot(x, y, label='y=sin(x)', color='red') # plot the graph
plt.title('Basic Plot', fontsize=16) # the name of plot at the top
plt.xlabel('x-axis', fontsize=12) # the name of x-axis
plt.ylabel('y-axis', fontsize=12) # the name of y-axis
plt.legend() # draw the labels at the right top
plt.grid(True) # draw a grid in the plot
plt.show() # show the plot
