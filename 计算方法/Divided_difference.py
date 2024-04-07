def divided_difference(x, y):
    """
    计算差商

    参数:
        x: 数据点的 x 坐标列表
        y: 数据点的 y 坐标列表

    返回值:
        一个包含所有差商的二维列表，其中每一行代表一个阶数的差商
    """
    n = len(x)
    # 初始化一个二维列表用于存储差商
    div_diff = [[0] * n for _ in range(n)]
    for i in range(n):
        div_diff[i][1] = y[i]
    for j in range(1, n):
        for i in range(n - j):  # 行
            div_diff[i][j] = (div_diff[i + 1][j - 1] - div_diff[i][j - 1]) / x[i + j] - x[i]
    return div_diff


# 示例数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 3, 2]

# 计算差商
diff = divided_difference(x, y)
# 输出差商
for i in range(len(diff)):
    print(f"阶数 {i}:", end=' ')
    for j in range(i + 1):
        print(diff[i][j], end=' ')
    print()
