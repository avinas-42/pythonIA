import numpy as np
def minmax(x):
    """Computes the normalized version of a non-empty numpy.array using the min-max standardization.
    Args:
    x: has to be an numpy.array, a vector.
    Return:
    x’ as a numpy.array.
    None if x is a non-empty numpy.array or not a numpy.array.
    None if x is not of the expected type.
    Raises:
    This function shouldn’t raise any Exception.
    """
    ret = []
    min = np.min(x)
    max = np.max(x)
    if max - min == 0:
        return None
    for elem in x:
        ret.append((elem - min) / (max - min))
    return ret
    