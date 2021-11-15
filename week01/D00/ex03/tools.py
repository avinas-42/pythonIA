import numpy as np
from numpy.core.numeric import ones


def test_type(values, type, size, ndim):
    if isinstance(values, type):
        if values.ndim != ndim:
            return False
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
    if not test_type(x, (np.ndarray, np.generic), 0, 2):
        return None
    intercept = np.ones([x.shape[0], 1])
    x = np.hstack((intercept, x))
    return x
