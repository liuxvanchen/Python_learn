import numpy as np

# setxor1d() 方法采用可选参数 assume_unique , 如果设置为 True 可以加快计算速度。 处理集合时应始终设置为 True。
# 将数组转换为集合
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
# 要查找两个数组的唯一值，请使用 union1d() 方法。就是去除重复值
newarr = np.union1d(arr1, arr2)
print(newarr)

# 要仅查找两个数组中都存在的值，请使用 intersect1d() 方法。
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

# 要仅查找第一组中不存在于秒组中的值，请使用 setdiff1d() 方法。
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
# 找到2有1没有的
newarr = np.setdiff1d(set2, set1, assume_unique=True)
print(newarr)

# 找到2有1没有，和1有2没有的
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
