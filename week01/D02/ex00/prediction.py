import numpy as np

def simple_predict(x, theta):
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
    y_hat = np.zeros(theta.shape)
    for i in range(m):
        y_hat[i] = theta[0]
    for i in range(m):
        for j in range(n):
            y_hat[i] += theta[j +1] * x[i][j]
    return y_hat

