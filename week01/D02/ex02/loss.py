import numpy as np

def square(x):
    return x**2

def loss_elem_(y, y_hat):
    if y.ndim == 1:
        y = np.array([y]).T
    if y_hat.ndim == 1:
        y_hat = np.array([y_hat]).T
    ret = y_hat - y
    ret = np.array(list(map(square, ret)))
    return ret



def loss_(y, y_hat):
    ret = loss_elem_(y, y_hat)
    ret = float(1/(2 * len(y)) * sum(ret))
    return ret