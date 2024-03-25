import numpy as np
#删除小数，并返回最接近零的浮点数。
arr=np.trunc([-3.1666,3.6667])
print(arr)

arr2=np.fix([-3.1666,3.6667])
print(arr2)

#around() 函数如果 >=5 则将前面的数字或小数加 1，否则什么也不做。
arr = np.around(3.1666, 2)#舍入到小数点后2位
print(arr)

#floor() 函数将小数四舍五入到最接近的小整数。
arr3=np.floor([-3.1666,3.6667])
print(arr3)

#ceil() 函数将小数四舍五入到最接近的大整数。
arr4=np.ceil([-3.1666,3.6667])
print(arr4)