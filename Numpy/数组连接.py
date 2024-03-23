import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[6, 7], [8, 9]])

#按行拼接，答案是1267、3489
newarr = np.concatenate((arr3, arr4), axis=1)
#按列拼接，答案是12、34、56、78
newarr2 = np.concatenate((arr3, arr4), axis=0)
print(newarr)
print(newarr2)

#沿着第二个轴使两个数组重叠，这将导致他们彼此重叠，142536
stackarr=np.stack((arr1,arr2),axis=1)
print(stackarr)

#沿行堆叠
harr=np.hstack((arr1,arr2))
print(harr)

#沿列堆叠
varr=np.vstack((arr1,arr2))
print(varr)

#沿高度堆叠
darr=np.dstack((arr1,arr2))
print(darr)
