import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import numpy as np


def get_input_number():
    num = input("enter some numbers with',': ")
    numbers = list(map(float, num.split(',')))
    return numbers


x = np.array([8.7, 12.3, 16.4, 19.7, 22.8, 26.9, 32.8, 36.5, 42.1])
#树高
# y = np.array([10.6, 14.0, 17.0, 19.3, 20.7, 21.6, 23.2, 24.0, 28.1])
#材积
y=np.array([ 0.034,0.090,0.175,0.274,0.376,0.556,0.831,1.101,1.477])
weights = np.array([9, 19, 11, 9, 3, 2, 3, 1, 1])
x_test = np.array([10.3, 12.8, 15.8, 19.2, 19.8, 22.5, 27.6, 26.0, 24.4])
#树高
#y_test = np.array([8.2, 11.8, 15.7, 20.6, 24.0, 28.9, 33.0, 41.5, 43.5])
#材积
y_test=np.array([0.032,0.073,0.149,0.298,0.403,0.666,1.095,1.125,1.374])

sigma = np.sqrt(weights)


def mean_relative_error(y_true, y_pred):
    n = len(y_true)
    mre = np.mean(np.abs((y_true - y_pred) / y))
    return mre


# 定义 linear model
def linear_func(x, a, b):
    return a * x + b


params, covariance = curve_fit(linear_func, x, y, sigma=sigma)

a, b = params

print("Slope:", a)
print("Intercept:", b)

plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']

plt.scatter(x, y, label='数据')
plt.plot(x, linear_func(x, a, b), color='red', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('H-D线性拟合')
plt.legend()
plt.show()

#  R^2
y_pred = linear_func(x, a, b)
r2 = r2_score(y, y_pred)

print("R^2:", r2)

y_test_pred = linear_func(x_test, a, b)
print(mean_relative_error(y_test, y_test_pred))
