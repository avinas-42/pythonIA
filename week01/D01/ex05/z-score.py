import numpy as np
def zscore(x):
    """Computes the normalized version of a non-empty numpy.array using the z-score standardization.
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
    mean = np.mean(x)
    std = np.std(x)
    for elem in x:
        ret.append((elem - mean) / std)
    return ret


# # Example 1:
# X = np.array([0, 15, -9, 7, 12, 3, -21])
# print(zscore(X))
# # Output:
# # array([-0.08620324, 1.2068453 , -0.86203236, 0.51721942, 0.94823559,
# # 0.17240647, -1.89647119])
# # Example 2:
# Y = np.array([2, 14, -13, 5, 12, 4, -19])

# print(zscore(Y))
# # Output:
# # array([ 0.11267619, 1.16432067, -1.20187941, 0.37558731, 0.98904659,
# # 0.28795027, -1.72770165])