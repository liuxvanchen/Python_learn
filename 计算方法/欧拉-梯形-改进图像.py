import numpy as np
import matplotlib.pyplot as plt


# 微分方程
def f(x, y):
    return x - y


# 欧拉方法
def euler_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


# 改进欧拉方法
def improved_euler_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n):
        y_predict = y + h * f(x, y)
        x_predict = x + h
        y += h * 0.5 * (f(x, y) + f(x_predict, y_predict))
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


# 梯形方法
def trapezoidal_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n):
        y_next = y + 0.5 * h * (f(x, y) + f(x + h, y + h * f(x, y)))
        for __ in range(5):  # 简单的固定次数迭代
            y_next = y + 0.5 * h * (f(x, y) + f(x + h, y_next))
        y = y_next
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


# 初始条件和步长
x0 = 0
y0 = 1
h = 0.1
n = 20  # 步数

# 计算每种方法的结果
x_euler, y_euler = euler_method(f, x0, y0, h, n)
x_improved, y_improved = improved_euler_method(f, x0, y0, h, n)
x_trap, y_trap = trapezoidal_method(f, x0, y0, h, n)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, label='欧拉方法', marker='o')
plt.plot(x_improved, y_improved, label='改进欧拉', marker='x')
plt.plot(x_trap, y_trap, label='梯形方法', marker='s')
plt.xlabel('x')
plt.ylabel('y')
plt.title('求解常微分方程的数值方法比较')
# 字体设置
plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']
plt.legend()
plt.grid(True)
plt.show()
