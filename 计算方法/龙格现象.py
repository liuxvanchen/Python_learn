import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# 定义龙格函数
def runge_function(x):
    return 1 / (1 + 25 * x**2)

# 插值点的数量
n_points = 11
# 等间距插值点
x_interp = np.linspace(-1, 1, n_points)
y_interp = runge_function(x_interp)

# 计算拉格朗日插值多项式
poly = Polynomial.fit(x_interp, y_interp, deg=n_points-1)

# 生成绘图点
x_plot = np.linspace(-1, 1, 1000)
y_plot = runge_function(x_plot)
y_poly = poly(x_plot)

# 绘图
plt.figure(figsize=(10, 6))
plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']
plt.plot(x_plot, y_plot, label='龙格函数', color='blue')
plt.plot(x_plot, y_poly, label='多项式插值', color='red')
plt.scatter(x_interp, y_interp, label='插值节点', color='black')
plt.title('龙格现象')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
