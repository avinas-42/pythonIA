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
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    Returns:
    x as a numpy.array, a vector of shape m * 2.
    None if x is not a numpy.array.
    None if x is a empty numpy.array.
    Raises:
    This function should not raise any Exception.
    """
    if not test_type(x, (np.ndarray, np.generic), 0):
        return None
    intercept = np.ones([x.shape[0], 1])
    x = np.hstack((intercept, x))
    return x


def predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of shape m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta shapes are not appropriate.
    None if x or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    ret = []

    if not test_type(x, (np.ndarray, np.generic), 0):
        return None
    if not test_type(theta, (np.ndarray, np.generic), 0):
        return None

    
    x = np.array([x]).T

    x = add_intercept(x)

    theta = theta.T

    ret = x * theta
    ret = np.sum(ret, axis=1)
    ret = np.array([ret]).T
    return ret


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

    if x.ndim == 1:
        x_transpose = np.array([x]).T
    x_prime = add_intercept(x_transpose)
    nab = np.dot(x_prime, theta) - y
    x_prime_transpose = x_prime.T

    nab = np.dot(x_prime_transpose, nab)
    nab = nab * (1 / len(y))

    return nab
