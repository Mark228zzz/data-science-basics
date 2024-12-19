import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider  # import Slider for interactivity

# generate data for interactive plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# create the main plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # adjust space for slider

# plot the initial data
l, = plt.plot(x, y, lw=2)

# add a slider below the plot
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Frequency', 0.1, 2.0, valinit=1)

def update(val):
    """Update the plot based on slider value."""
    freq = slider.val  # get current slider value
    l.set_ydata(np.sin(freq * x))  # update y data with new frequency
    fig.canvas.draw_idle()  # redraw the figure

slider.on_changed(update)  # connect slider to update function
plt.show()
