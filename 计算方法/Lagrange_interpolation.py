def lagrange_interpolation(x, y, x_interp):
    result = 0.0
    n = len(x)
    for i in range(n):
        f1 = 1.0  # 初始化 f1
        f2 = 1.0  # 初始化 f2
        for j in range(n):
            if j != i:
                f1 *= (x_interp - x[j])
                f2 *= (x[i] - x[j])
        result += y[i] * (f1 / f2)
    return result


x_interp = 2.5
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 3, 2]

result = lagrange_interpolation(x, y, x_interp)
print(result)
