def euler_method(f, x0, y0, h, x_end):
    """
    使用欧拉方法解常微分方程 dy/dx = f(x, y)。

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
        y += h * f(x, y)  # 更新y值
        x += h  # 更新x值
        xs.append(x)
        ys.append(y)

    return xs, ys


# 示例: 解决 dy/dx = x + y, 初始条件 y(0) = 1
f = lambda x, y: x + y # 匿名函数
x0 = 0
y0 = 1
h = 0.1  # 步长
x_end = 2  # 积分结束的x值

# 使用欧拉方法
xs, ys = euler_method(f, x0, y0, h, x_end)

# 打印结果
for x, y in zip(xs, ys):
    print(f"x={x:.2f}, y={y:.2f}")
