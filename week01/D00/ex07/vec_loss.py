import numpy as np


def square(x):
    return x**2

def loss_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_elem: numpy.array, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between y and y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if y.ndim == 1:
        y = np.array([y]).T
    if y_hat.ndim == 1:
        y_hat = np.array([y_hat]).T
    ret = y_hat - y
    ret = np.array(list(map(square, ret)))
    return ret


def loss_(y, y_hat):
    """
    Description:
    Calculates the value of loss function.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a shape matching problem between y or y_hat.
    None if y or y_hat is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    ret = loss_elem_(y, y_hat)
    ret = float(1/(2 * len(y)) * sum(ret))
    return ret
