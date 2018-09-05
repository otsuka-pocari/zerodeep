import numpy as np
import matplotlib.pylab as plt

def rele_function(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = rele_function(x)
plt.plot(x, y)
plt.ylim(-1, 6)
plt.show()
