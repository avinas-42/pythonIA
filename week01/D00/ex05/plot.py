import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    mult = np.linspace(1, 5, 10)
    plt.plot(x, y, 'o')
    plt.plot(mult, theta[0] + theta[1] * mult)
    plt.show()
