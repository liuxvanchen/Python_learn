import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[2] + arr[3])

# 二位数组创建，加逗号
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 访问第一维的第二个数
print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])

# 三维
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12, ]]])
# 第一个维度有两个数组，第二个维度有两个数组，第三个维度有三个数
print(arr[0, 1, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# 打印第二个维度的最后一个元素
print('Last element from 2nd dim: ', arr[1, -1])
