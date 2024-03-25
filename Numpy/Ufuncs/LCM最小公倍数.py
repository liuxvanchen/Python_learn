import numpy as np
from functools import reduce

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

#找多个数字的最小公倍数
arr=np.array([3,6,9])
#reduce() 方法将使用 ufunc，在本例中为 lcm() 函数，on 每个元素，并将数组减少一维。
x2=np.lcm.reduce(arr)
print(x2)

arr2=np.arange(1,10)
x3=np.lcm.reduce(arr2)
print(x3)