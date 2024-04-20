import numpy as np

x = np.array([8.7, 12.3, 16.4, 19.7, 22.8, 26.9, 32.8, 36.5, 42.1])
y = np.array([10.6, 14.0, 17.0, 19.3, 20.7, 21.6, 23.2, 24.0, 28.1])

y_mean=y.mean()
x_mean=x.mean()
print(x_mean)
print(y_mean)

# 计算斜率 a
a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

# 计算截距 b
b = y_mean - a * x_mean

print(a,b)

def calculate_power_function(x_points, y_points):
    # 将数据转换为 numpy 数组并取对数
    log_x = np.log(x_points)
    log_y = np.log(y_points)

    # 计算 log(x) 和 log(y) 的平均值
    log_x_mean = np.mean(log_x)
    log_y_mean = np.mean(log_y)

    # 计算斜率 b
    b = np.sum((log_x - log_x_mean) * (log_y - log_y_mean)) / np.sum((log_x - log_x_mean) ** 2)

    # 计算截距 log(a)
    log_a = log_y_mean - b * log_x_mean

    # 计算系数 a
    a = np.exp(log_a)

    return a, b


# 计算参数
a, b = calculate_power_function(x, y)
print(a,b)
