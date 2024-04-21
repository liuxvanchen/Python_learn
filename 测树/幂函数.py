import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

x = np.array([8.7, 12.3, 16.4, 19.7, 22.8, 26.9, 32.8, 36.5, 42.1])
#树高
y = np.array([10.6, 14.0, 17.0, 19.3, 20.7, 21.6, 23.2, 24.0, 28.1])
#材积
# y=np.array([ 0.034,0.090,0.175,0.274,0.376,0.556,0.831,1.101,1.477])
weights = np.array([9, 19, 11, 9, 3, 2, 3, 1, 1])
x_test = np.array([10.3, 12.8, 15.8, 19.2, 19.8, 22.5, 27.6, 26.0, 24.4])
#树高
y_test = np.array([8.2, 11.8, 15.7, 20.6, 24.0, 28.9, 33.0, 41.5, 43.5])
#材积
# y_test=np.array([0.032,0.073,0.149,0.298,0.403,0.666,1.095,1.125,1.374])

sigma = np.sqrt(weights)



def mean_relative_error(y_true, y_pred):
    n = len(y_true)
    mre = np.mean(np.abs((y_true - y_pred) / y_true))
    return mre


# 定义幂函数模型
def power_func(x, a, b):
    return a * np.power(x, b)


# 使用 curve_fit 函数进行拟合
params, covariance = curve_fit(power_func, x, y, sigma=sigma)

# 获取拟合的参数
a, b = params

# 打印拟合的参数
print("a:", a)
print("b:", b)

# 绘制原始数据和拟合曲线
plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']

plt.scatter(x, y, label='数据')
plt.plot(x, power_func(x, a, b), color='red', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('树高-胸径幂函数拟合')
plt.legend()
plt.show()

y_pred = power_func(x, a, b)
y_test_pred=power_func(x_test,a,b)

# 计算 R^2
r2 = r2_score(y, y_pred)
print("R^2:", r2)
# 计算MRE
print(mean_relative_error(y_test, y_test_pred))
