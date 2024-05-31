import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 定义目标函数
def target_function(x):
    return np.exp(x)

# 定义多项式逼近函数
def polynomial_approx(x, coeffs):
    # 计算多项式的值
    return sum(c * x**i for i, c in enumerate(coeffs))

# 定义逼近误差的最大值函数
def max_error(coeffs, *args):
    x_vals = args[0]
    y_true = target_function(x_vals)
    y_approx = polynomial_approx(x_vals, coeffs)
    # 返回最大绝对误差
    return np.max(np.abs(y_true - y_approx))

# 设置用于逼近的x值（均匀分布）
x_values = np.linspace(-1, 1, 500)

# 初始多项式系数猜测（这里我们使用二次多项式）
initial_coeffs = np.zeros(3)

# 使用minimize函数进行优化
result = minimize(max_error, initial_coeffs, args=(x_values,), method='Powell')

# 获取优化后的系数
optimized_coeffs = result.x

# 绘制结果
plt.figure(figsize=(10, 5))
plt.plot(x_values, target_function(x_values), label='Target Function $e^x$')
plt.plot(x_values, polynomial_approx(x_values, optimized_coeffs), label='Best Uniform Approximation')
plt.legend()
plt.grid(True)
plt.title('Best Uniform Approximation of $e^x$ on [-1, 1]')
plt.show()

print("Optimized coefficients:", optimized_coeffs)
