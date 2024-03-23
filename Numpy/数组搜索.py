#使用where方法
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr == 4)
#查找偶数
y=np.where(arr%2==0)
print(x)
print(y)

#在数组中执行二进制搜索，并返回将在其中插入指定值以维持搜索顺序的索引。
arr2=np.array([6,7,8,9])
#默认情况下，返回最左边的索引，但是我们可以给定 side='right'，以返回最右边的索引。
i=np.searchsorted(arr2,7,side='right')
print(i)

#插入多个值
j=np.searchsorted(arr2,[1,2,3])
print(j)