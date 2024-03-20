import numpy as np

arr=np.array([1,2,3])
print(arr.dtype)
arr2=np.array(['appllle','pear'])
print(arr2.dtype)#U后面的数字表示最大的长度

#用自己定义的数据类型创建数组
myarr=np.array([1,2,3,4],dtype='S')
print(myarr)
print(myarr.dtype)