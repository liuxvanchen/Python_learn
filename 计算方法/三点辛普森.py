def f(x):
    # 定义需要积分的函数
    return x**2

def simpsons_rule(f, a, b, n):
    """
    使用三点辛普森法计算定积分

    参数：
    f：要积分的函数
    a：积分下限
    b：积分上限
    n：划分区间的数量，必须为偶数

    返回值：
    积分的近似值
    """
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    x = a
    integral = f(a) + f(b)

    for i in range(1, n):
        coefficient = 2 if i % 2 == 0 else 4
        x += h
        integral += coefficient * f(x)

    integral *= h / 3

    return integral

# 要积分的区间和划分数量
a = 0
b = 2
n = 10

# 使用三点辛普森法计算积分
integral_approx = simpsons_rule(f, a, b, n)
print("Approximate value of the integral:", integral_approx)
