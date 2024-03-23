import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
#可以通过索引进行单个访问
print(newarr[1])
arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new=np.array_split(arr2,2,axis=1)
print(new)