def f(x):
    # 定义需要积分的函数
    return x**2

def trapezoidal_rule(f, a, b, n):
    """
    使用梯形公式计算定积分

    参数：
    f：要积分的函数
    a：积分下限
    b：积分上限
    n：划分区间的数量

    返回值：
    积分的近似值
    """
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h

    return integral

# 要积分的区间和划分数量
a = 0
b = 2
n = 10

# 使用梯形公式计算积分
integral_approx = trapezoidal_rule(f, a, b, n)
print("Approximate value of the integral:", integral_approx)
