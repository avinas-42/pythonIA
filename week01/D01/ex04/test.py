import pandas as pd
import numpy as np

from linear_model import MyLinearRegression as MyLR

data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data['Micrograms']).reshape(-1,1)
Yscore = np.array(data['Score']).reshape(-1,1)
# Example 1:
linear_model1 = MyLR(np.array([[89.0], [-8]]))
Y_model1 = linear_model1.predict_(Xpill)
print(linear_model1.mse_(Yscore, Y_model1))

linear_model1.fit_(Xpill, Yscore)
Y_model1 = linear_model1.predict_(Xpill)
# linear_model1.plotJ(Xpill, Yscore)

# Output:
# 57.60304285714282
# 57.60304285714282
# Example 2:
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model2 = linear_model2.predict_(Xpill)
print(linear_model2.mse_(Yscore, Y_model2))
linear_model2.fit_(Xpill, Yscore)
Y_model2 = linear_model2.predict_(Xpill)
linear_model2.plotJ(Xpill, Yscore)

# Output:
# 232.16344285714285
# 232.16344285714285