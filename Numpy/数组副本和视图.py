import numpy as np

arr = np.array([1, 2, 3, 4])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)  # copy的数组不会因为对原数组做了操作而改变

y = arr.view()
arr[1] = 99
print(arr)
print(y)  # 视图会随着原数组的改变而改变

# 打印base属性来检查数组是否拥有自己的数据
print(x.base)  # None
print(y.base)  # 数组数据
