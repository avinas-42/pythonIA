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

def predict_(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a matrix of shape m * n.
    theta: has to be an numpy.array, a vector of shape (n + 1) * 1.
    Return:
    y_hat as a numpy.array, a vector of shape m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta shapes are not appropriate.
    None if x or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    m, n = x.shape
    # if theta.ndim == 1: 
    #         theta = np.array([theta]).T
    y_hat = np.zeros(theta.shape)
    x_prime = add_intercept(x)
    if theta.ndim != 1:
        theta = theta.T
    y_hat = x_prime * theta
    return y_hat.sum(axis=1)

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


def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.array, a matrix of shape m * n:
    (number of training examples, number of features).
    y: has to be a numpy.array, a vector of shape m * 1:
    (number of training examples, 1).
    theta: has to be a numpy.array, a vector of shape (n + 1) * 1:
    (number of features + 1, 1).
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Return:
    new_theta: numpy.array, a vector of shape (number of features + 1, 1).
    None if there is a matching shape problem.
    None if x, y, theta, alpha or max_iter is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    tmptheta = theta

    while(max_iter > 0):
        nabs = gradient(x, y, tmptheta)
        for i in range(len(nabs)):
            nabs[i] = nabs[i] * alpha
            tmptheta[i] = tmptheta[i] - nabs[i]
        max_iter -= 1
    return np.array(tmptheta)
