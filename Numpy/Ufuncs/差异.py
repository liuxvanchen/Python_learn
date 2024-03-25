#离散差意味着减去两个连续的元素。例如 对于 [1, 2, 3, 4]，离散差为 [2-1, 3-2, 4-3] = [1, 1, 1]
import numpy as np

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
#指定计算离散差的次数：n=2
newarr2 = np.diff(arr, n=2)
print(newarr2)