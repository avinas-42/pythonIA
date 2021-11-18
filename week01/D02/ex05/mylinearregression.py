import numpy as np
import matplotlib.pyplot as plt

def square(x):
    return x**2

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = np.array(thetas)
        
            
    
    @staticmethod
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
    
    @staticmethod
    def loss_elem_(y, y_hat):
        if y.ndim == 1:
            y = np.array([y]).T
        if y_hat.ndim == 1:
            y_hat = np.array([y_hat]).T
        ret = y_hat - y
        ret = np.array(list(map(square, ret)))
        return ret


    @staticmethod
    def loss_(y, y_hat):
        ret = MyLinearRegression.loss_elem_(y, y_hat)
        ret = float(1/(2 * len(y)) * sum(ret))
        return ret

    @staticmethod
    def add_intercept(x):
        if not MyLinearRegression.test_type(x, (np.ndarray, np.generic), 0):
            return None
        intercept = np.ones([x.shape[0], 1])
        x = np.hstack((intercept, x))
        return x

    def predict_(self, x):
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
        # if theta.ndim == 1: 
        #         theta = np.array([theta]).T
        y_hat = np.zeros(self.thetas.shape)
        x_prime = MyLinearRegression.add_intercept(x)
        if self.thetas.ndim != 1:
            theta = self.thetas.T
        
        y_hat = x_prime * theta
        y_hat = y_hat.sum(axis=1)
        if y_hat.ndim == 1:
            y_hat = np.array([y_hat]).T
        return y_hat
    @staticmethod
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

        if not MyLinearRegression.test_type(x, (np.ndarray, np.generic), 0):
            return None
        if not MyLinearRegression.test_type(y, (np.ndarray, np.generic), 0):
            return None
        if not MyLinearRegression.test_type(theta, (np.ndarray, np.generic), 0):
            return None
        x_transpose = x
        
        if x.ndim == 1:
            x_transpose = np.array([x]).T
        x_prime = MyLinearRegression.add_intercept(x_transpose)
        
        nab = np.dot(x_prime, theta) - y
        x_prime_transpose = x_prime.T

        nab = np.dot(x_prime_transpose, nab)
        nab = nab * (1 / len(y))

        return nab

    def fit_(self, x, y):
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
        tmptheta = self.thetas
        max_iter = self.max_iter
        while(max_iter > 0):
            nabs = MyLinearRegression.gradient(x, y, tmptheta)
            for i in range(len(nabs)):
                nabs[i] = nabs[i] * self.alpha
                tmptheta[i] = tmptheta[i] - nabs[i]
            max_iter -= 1
        self.thetas = np.array(tmptheta)
