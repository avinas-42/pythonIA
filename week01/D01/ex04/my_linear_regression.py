import numpy as np

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
        self.thetas = np.array([[thetas[0]], [thetas[1]]], dtype=np.float64)

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
    def add_intercept(x):
        if not MyLinearRegression.test_type(x, (np.ndarray, np.generic), 0):
            return None
        intercept = np.ones([x.shape[0], 1])
        x = np.hstack((intercept, x))
        return x

    def predict_(self, x):
        ret = []
        if not MyLinearRegression.test_type(x, (np.ndarray, np.generic), 0):
            return None

        if x.ndim == 1: 
            x = np.array([x]).T
        
        x = MyLinearRegression.add_intercept(x)
        if self.thetas.shape[0] > self.thetas.shape[1]:
            self.thetas = self.thetas.T
        
        ret = x * self.thetas
        ret = np.sum(ret, axis=1)
        ret = np.array([ret]).T
        return ret
    
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
    def gradient(x, y, theta):
        if not MyLinearRegression.test_type(x, (np.ndarray, np.generic), 0):
            return None
        if not MyLinearRegression.test_type(y, (np.ndarray, np.generic), 0):
            return None
        if not MyLinearRegression.test_type(theta, (np.ndarray, np.generic), 0):
            return None
        
        y_transpose = y.T[0]
        x_prime = MyLinearRegression.add_intercept(x)
        nab = np.dot(x_prime, theta) - y_transpose
        
        
        x_prime_transpose = x_prime.T

        nab = np.dot(x_prime_transpose, nab)
        nab = nab * (1 / len(y_transpose))

        return nab

    def fit_(self, x, y):
      
        theta0 = self.thetas[0][0]
        theta1 = self.thetas[1][0]
        max_iter = self.max_iter
        while(max_iter > 0):
            nab = MyLinearRegression.gradient(x, y, np.array([theta0, theta1]))
            nab0 = nab[0] * self.alpha
            nab1 = nab[1] * self.alpha
            theta0 = theta0 - nab0
            theta1 = theta1 - nab1
            max_iter -= 1
        self.thetas[0] = theta0
        self.thetas[1] = theta1