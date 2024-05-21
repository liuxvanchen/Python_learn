# 定义步长
h = 0.2

# 定义微分方程
def f(x, y):
    return 2 * x - y

# 初始条件
x0 = 0
y0 = 1

# 四阶龙格-库塔方法计算 y(0.2)
def runge_kutta_4_step(f, x0, y0, h):
    k1 = f(x0, y0)
    k2 = f(x0 + h / 2, y0 + k1 * h / 2)
    k3 = f(x0 + h / 2, y0 + k2 * h / 2)
    k4 = f(x0 + h, y0 + k3 * h)
    y_next = y0 + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    print(k1,k2,k3,k4)
    return y_next

# 计算 y(0.2)
y_02 = runge_kutta_4_step(f, x0, y0, h)
print(y_02)
