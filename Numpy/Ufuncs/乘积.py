import numpy as np
from functools import reduce

arr = np.array([1, 2, 3, 4])
#连乘，所有的元素
x = np.prod(arr)
print(x)

x2=reduce(lambda x,y:x*y,arr)
print(x2)

arr2=np.array([5,6,7,8])
y=np.prod([arr,arr2])
print(y)

y1=np.prod([arr,arr2],axis=1)#对行也就是每一个数组内部元素求乘积
y2=np.prod([arr,arr2],axis=0)#对列也就是对应位置求乘积
print(y1,'\n',y2)

arr = np.array([5, 6, 7, 8])
#部分求乘积[   5   30  210 1680]
newarr = np.cumprod(arr)
print(newarr)