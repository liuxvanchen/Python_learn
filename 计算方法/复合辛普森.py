def f(x):
    # 定义被积函数，这里以 f(x) = x^2 作为示例
    return x ** 2


def composite_simpson(a, b, n):
    """
    使用复合辛普森公式求积分

    参数:
    a, b : 数值积分的上下限
    n    : 子区间的数量，n 必须是偶数

    返回:
    积分的近似值
    """
    if n % 2 == 1:
        raise ValueError("复合辛普森规则要求区间数 n 必须为偶数")

    h = (b - a) / n
    x = a
    S = f(a) + f(b)

    # 计算中间点的函数值，交替乘以 4 和 2
    for i in range(1, n):
        x += h
        if i % 2 == 0:
            S += 2 * f(x)
        else:
            S += 4 * f(x)

    return S * h / 3


# 设置积分的上下限和子区间数
a = 0  # 积分下限
b = 1  # 积分上限
n = 100  # 子区间数，必须是偶数

# 计算积分并打印结果
integral = composite_simpson(a, b, n)
print(f"积分的近似值为: {integral}")
