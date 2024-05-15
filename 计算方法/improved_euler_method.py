def improved_euler_method(f, x0, y0, h, x_end):
    """
    使用改进欧拉方法解常微分方程 dy/dx = f(x, y)。

    参数:
    f : 微分方程右侧的函数，f(x, y)。
    x0 : 初始x值。
    y0 : 初始y值。
    h : 步长。
    x_end : 积分结束的x值。

    返回:
    xs, ys : x和y的值列表，表示数值解。
    """
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0

    while x < x_end:
        # 预测步骤
        y_predict = y + h * f(x, y)
        x_predict = x + h

        # 校正步骤
        y += h * 0.5 * (f(x, y) + f(x_predict, y_predict))
        x += h

        xs.append(x)
        ys.append(y)

    return xs, ys


# 示例: 解决 dy/dx = x - y, 初始条件 y(0) = 1
f = lambda x, y: x - y
x0 = 0
y0 = 1
h = 0.1  # 步长
x_end = 2  # 积分结束的x值

# 使用改进欧拉方法
xs, ys = improved_euler_method(f, x0, y0, h, x_end)

# 打印结果
for x, y in zip(xs, ys):
    print(f"x={x:.2f}, y={y:.2f}")
