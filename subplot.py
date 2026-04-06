import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(x, y1)
axs[0].set_title("Sine Wave")
axs[1].plot(x, y2)
axs[1].set_title("Cosine Wave")
plt.tight_layout()
plt.show()