import numpy as np


def test_type(values, type, size):
    if isinstance(values, type):
        ret = True
        if size > 0:
            if values.shape[0] != size:
                ret = False
        elif values.shape[0] < 1:
            ret = False
        return ret


def simple_predict(x, theta):
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
    if not test_type(theta, (np.ndarray, np.generic), 2):
        return None
    for val in x:
        ret.append(theta[0] + theta[1] * val)

    return ret
