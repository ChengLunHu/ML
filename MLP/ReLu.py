import numpy
from pylab import *

floatX = 'float32'
def relu(x):
    """
    relu implementation with T.maximum
    Parameters
    ----------
    x: tensor variable
    """
    return numpy.maximum(x, zeros(x.shape))

def relu_(x):
    """
    Alternative relu implementation
    Parameters
    ----------
    x: tensor variable
    """
    return x * (x > 0)

t = arange(-20, 20, 1)
y0 = relu(t)
y1 = relu_(t-10)

subplot(211)
plot(t, y0, color='k')
xlabel('x')
ylabel('y')
axis([min(t), max(t), min(y0), max(y0)])

subplot(212)
plot(t, y1, color='k')
xlabel('x')
ylabel('y')
axis([min(t), max(t), min(y1), max(y1)])

show()
