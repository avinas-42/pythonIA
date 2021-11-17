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

    if x.ndim == 1:
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
    
    y_transpose = y.T[0]
    x_prime = add_intercept(x)
    nab = np.dot(x_prime, theta) - y_transpose
    
    
    x_prime_transpose = x_prime.T

    nab = np.dot(x_prime_transpose, nab)
    nab = nab * (1 / len(y_transpose))

    return nab

def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
    y: has to be a numpy.array, a vector of shape m * 1: (number of training examples, 1).
    theta: has to be a numpy.array, a vector of shape 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Return:
    new_theta: numpy.array, a vector of shape 2 * 1.
    None if there is a matching shape problem.
    None if x, y, theta, alpha or max_iter is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    theta0 = theta[0]
    theta1 = theta[1]
    while(max_iter > 0):
        nab = gradient(x, y, np.array([theta0, theta1]))
        nab0 = nab[0] * alpha
        nab1 = nab[1] * alpha
        theta0 = theta0 - nab0
        theta1 = theta1 - nab1

        max_iter -= 1
    return np.array([[theta0],[theta1]])
