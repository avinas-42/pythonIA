import numpy as np

def test_type(values, type, size):
    if isinstance(values, type):
        if size > 0:
            if values.shape[0] != size:
                return False
        elif values.shape[0] < 1:
            return False
    else:
        return False
    return True

def add_intercept(x):
    if not test_type(x, (np.ndarray, np.generic), 0):
        return None
    intercept = np.ones([x.shape[0], 1])
    x = np.hstack((intercept, x))
    return x

def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for-loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a 2 * 1 vector.
    Return:
    The gradient as a numpy.array, a vector of shape 2 * 1.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible shapes.
    None if x, y or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """

    if not test_type(x, (np.ndarray, np.generic), 0):
        return None
    if not test_type(y, (np.ndarray, np.generic), 0):
        return None
    if not test_type(theta, (np.ndarray, np.generic), 0):
        return None
    x_transpose = x
    if x.ndim == 1:
        x_transpose = np.array([x]).T
    x_prime = add_intercept(x_transpose)
    nab = np.dot(x_prime, theta) - y
    x_prime_transpose = x_prime.T

    nab = np.dot(x_prime_transpose, nab)
    nab = nab * (1 / len(y))

    return nab
