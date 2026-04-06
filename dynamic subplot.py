%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

x = np.linspace(0, 10, 100)

line1, = axs[0].plot([], [])
line2, = axs[1].plot([], [])

axs[0].set_xlim(0, 10)
axs[0].set_ylim(-1, 1)
axs[0].set_title("Sine Wave")

axs[1].set_xlim(0, 10)
axs[1].set_ylim(-1, 1)
axs[1].set_title("Cosine Wave")
def update(frame):
    y1 = np.sin(x + frame * 0.1)
    y2 = np.cos(x + frame * 0.1)
    
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    
    return line1, line2
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)
HTML(ani.to_jshtml())