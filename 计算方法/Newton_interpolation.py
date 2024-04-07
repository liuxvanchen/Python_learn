def newton_interpolation(x, y, x_interp):
    """
    使用牛顿插值法对给定的数据点进行插值计算

    参数:
        x: 已知数据点的 x 坐标列表
        y: 已知数据点的 y 坐标列表
        x_interp: 插值计算的目标 x 坐标

    返回值:
        对应于 x_interp 的插值计算结果
    """
    n = len(x)
    # 初始化差商表
    div_diff = [[0] * n for _ in range(n)]
    # 将 y 坐标值赋值给第一列
    for i in range(n):
        div_diff[i][0] = y[i]
    # 计算差商表
    for j in range(1, n):
        for i in range(n - j):
            div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / (x[i + j] - x[i])
    # 初始化插值结果
    result = div_diff[0][0]
    # 计算插值
    for j in range(1, n):
        term = 1
        for i in range(j):
            term *= (x_interp - x[i])
        result += div_diff[0][j] * term
    return result

# 示例数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 3, 2]

# 插值计算
x_interp = 2.5
result = newton_interpolation(x, y, x_interp)
print(f'在 x = {x_interp} 处的插值结果为: {result}')

# from Divided_difference import divided_difference
#
# def newton_interpolation(x, y, x_interp):
#     """
#         使用牛顿插值法对给定的数据点进行插值计算
#
#         参数:
#             x: 已知数据点的 x 坐标列表
#             y: 已知数据点的 y 坐标列表
#             x_interp: 插值计算的目标 x 坐标
#
#         返回值:
#             对应于 x_interp 的插值计算结果
#         """
#     n = len(x)
#     div_diff=divided_difference(x,y)
#     result=div_diff[0][0]
#     for j in range(1, n):
#         term = 1
#         for i in range(j):
#             term *= (x_interp - x[i])
#         result += div_diff[0][j] * term
#     return result
#
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 4, 3, 2]
#
# # 插值计算
# x_interp = 2.5
# result = newton_interpolation(x, y, x_interp)
# print(f'在 x = {x_interp} 处的插值结果为: {result}')


