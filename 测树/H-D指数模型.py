import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# 给定的数据点
x = np.array([8.7, 12.3, 16.4, 19.7, 22.8, 26.9, 32.8, 36.5, 42.1])
y = np.array([0.034, 0.090, 0.175, 0.274, 0.376, 0.556, 0.831, 1.101, 1.477])

# 测试数据
x_test = np.array([10.3, 12.8, 15.8, 19.2, 19.8, 22.5, 27.6, 26.0, 24.4])
y_test = np.array([0.032, 0.073, 0.149, 0.298, 0.403, 0.666, 1.095, 1.125, 1.374])

# 对y取自然对数
ln_y = np.log(y)

# 使用线性回归拟合对数转换后的数据
b, ln_a = np.polyfit(x, ln_y, 1)

# 从线性回归结果中得到指数模型的参数
a = np.exp(ln_a)

# 定义指数模型函数
def exp_model(x):
    return a * np.exp(b * x)

# 计算测试集的预测值
y_pred_test = exp_model(x_test)

r2 = r2_score(y_test, y_pred_test)

print("R²值:", r2)

# 定义平均相对误差函数
def mean_relative_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true))

# 计算MRE
mre_test = mean_relative_error(y_test, y_pred_test)

# 打印模型参数和测试集的MRE
print(a, b, mre_test)

plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']

# 绘制原始数据点
plt.scatter(x, y, label='原始数据')

# 绘制指数拟合曲线
x_line = np.linspace(min(x), max(x), 100)
y_line = exp_model(x_line)
plt.plot(x_line, y_line, color='red', label='指数拟合曲线')

plt.xlabel('x')
plt.ylabel('y')
plt.title('材积-胸径指数拟合')
plt.legend()
plt.grid(True)
plt.show()
