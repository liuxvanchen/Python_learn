import numpy as np
from functools import reduce

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
#add是对两个数组相同位置的数进行相加
newarr = np.add(arr1, arr2)

print(newarr)

#将两个数组里面的值都加起来
sunarr=np.sum([arr1,arr2])
print(sunarr)

#指定轴。axis=1是对每个数组里面的元素求和，axis=0是对对应位置求和
axisarr=np.sum([arr1,arr2],axis=1)#[6 6]
axisarr2=np.sum([arr1,arr2],axis=0)#[2 4 6]
print(axisarr,'\n',axisarr2)

#累计和
addarr=np.cumsum(arr1)
print(addarr)

x1=np.arange(1,100)
y=reduce(lambda x,y:x+y,arr1)
print(y)