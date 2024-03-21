import numpy as np

arr=np.array([1,2,3])
print(arr.dtype)
arr2=np.array(['appllle','pear'])
print(arr2.dtype)#U后面的数字表示最大的长度

#用自己定义的数据类型创建数组
myarr=np.array([15,2,3,4],dtype='S')
print(myarr)
print(myarr.dtype)#S是字符串，数组里面的元素最长为多少就显示多少

myarrs=np.array([1,2,3,4],'i4')
print(myarrs)
print(myarrs.dtype)
#如果无法强制进行数据类型转换，那么会报错valueerror

arrpear=np.array([1.1,2.2,3.3])
print(arrpear.dtype)
#astype来创建数组副本并且更改数据类型
newarr=arrpear.astype('i')#还可以在括号里写int，bool来更改
print(newarr)
print(newarr.dtype)