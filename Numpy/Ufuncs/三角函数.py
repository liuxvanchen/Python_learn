import numpy as np

x = np.sin(np.pi / 2)
print(x)

# 查找 arr 中所有值的正弦值
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sin(arr)
print(x)

# 将度数转换为弧度
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# 弧度到度数
arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x = np.rad2deg(arr)
print(x)

# 根据正弦、余弦、正切的值求角度。 例如。 sin、cos 和 tan 逆（arcsin、arccos、arctan）
x = np.arcsin(1.0)
print(x)

# 数组中每个值的角度
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

# 在 NumPy 中使用勾股定理寻找斜边。
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
