import numpy as np

arr=np.array([3,2,5,1])
print(np.sort(arr))
print((np.sort(arr)).base)#返回的是副本

arr2=np.array(['apple','zanana','pear'])
print(np.sort(arr2))

arr3 = np.array([True, False, True])
print(np.sort(arr3))#false在前 ture在后

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))#分别对每行进行排序