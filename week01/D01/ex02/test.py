import numpy as np
from fit import fit_

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


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1, 1])
# Example 0:
theta1 = fit_(x, y, theta, alpha=5e-6, max_iter=15000)
print(theta1)
# Output:
# array([[1.40709365],
# [1.1150909 ]])
# Example 1:
ret = predict(x, theta1)
print(ret)
# Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])