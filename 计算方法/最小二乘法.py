import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义模型函数，x 是自变量，a 和 b 是要拟合的参数
def model(x, a, b):
    return a * x + b

# 生成一些模拟数据
np.random.seed(0)
x = np.arange(1, 10, 1)
y = 2.5 * x + 1.3 + np.random.normal(size=len(x))

# 使用 curve_fit 进行拟合
params, covariance = curve_fit(model, x, y)

# 拟合得到的参数
a_fitted, b_fitted = params
print("Fitted parameters: a =", a_fitted, ", b =", b_fitted)

# 使用拟合参数生成 y 值
y_fitted = model(x, *params)

# 绘图展示
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data')
plt.plot(x, y_fitted, label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Least Squares Fit to a Line')
plt.legend()
plt.show()
