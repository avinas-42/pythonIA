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

    y_hat = np.zeros(theta.shape)
    x_prime = add_intercept(x)
    
    y_hat = x_prime * theta
    return y_hat.sum(axis=1)
