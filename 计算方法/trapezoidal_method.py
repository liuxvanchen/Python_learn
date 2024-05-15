import numpy as np

def trapezoidal_method(f, x0, y0, h, x_end):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0

    while x < x_end:
        y_next = y + 0.5 * h * (f(x, y) + f(x + h, y + h * f(x, y)))  # 预测下一个y值
        # 对y_next进行简单的迭代修正
        for _ in range(5):  # 使用几次迭代来改进y_next的估计
            y_next = y + 0.5 * h * (f(x, y) + f(x + h, y_next))
        y = y_next
        x += h
        xs.append(x)
        ys.append(y)

    return xs, ys

# 示例微分方程 f(x, y) = -2y
f = lambda x, y: -2 * y
x0 = 0
y0 = 1  # 初始条件 y(0) = 1
h = 0.1  # 步长
x_end = 2  # 积分结束的x值

# 使用梯形方法
xs, ys = trapezoidal_method(f, x0, y0, h, x_end)

# 打印结果
for x, y in zip(xs, ys):
    print(f"x={x:.2f}, y={y:.2f}")
