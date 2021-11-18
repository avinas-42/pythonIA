import numpy as np
from vec_loss import loss_
X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
# Example 1:
ret = loss_(X, Y)
print(ret)
# Output:
# 2.142857142857143
# Example 2:
ret = loss_(X, X)
print(ret)
# Output:
# 0.0