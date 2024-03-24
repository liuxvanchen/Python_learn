from numpy import random
import numpy as np

arr=np.array([1,2,3,4,5])
#在数组本身中改变数组顺序
random.shuffle(arr)
print(arr)

#不改变原数组来生成数组排列
print(random.permutation(arr))
print(arr)