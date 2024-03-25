import numpy as np
from math import log

arr=np.arange(1,10)
#arange(1, 10) 函数返回一个从 1（包括）到 10（不包括）的整数数组。
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

#自定义log的底，使用前面学的frompyfunc创建一个ufunc函数
nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))

#以2 为底，log2 8
print(log(8,2))