from numpy import *
# from pylab import *
from matplotlib import pyplot as plt

def sigmoid(x):
    return 1 / (1 + exp(-x))

x = arange(-10, 10, 1)
sig = sigmoid(x)

plt.plot(x, sig)
plt.show()
