import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr = arr.reshape(3, 3)
print(newarr)
# 不能随意分割重塑
# newarr2=arr.reshape(2,2)
# print(newarr2)
print(newarr.base)  # 返回原始数组，是一个视图
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 可以使用位置的维度，自动计算
freearr = arr2.reshape(2, 2, -1)
print(freearr)
# 展平数组：将多维转为一维数组,reshape(-1)
freenewarr = arr.reshape(-1)
print(freenewarr)
