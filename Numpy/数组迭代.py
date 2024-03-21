import numpy as np
arr=np.array([1,2,3,4,5,6])
for x in arr:
    print(x)

arr2=np.array([[1,2,3],[4,5,6]])
for y in arr2:
    print(y)#将遍历每一行

#在三维数组遍历中，将遍历所有二维数组
arr3=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[12,13,45],[56,78,89],[55,11,22]]])
for i in arr3:
    print(i)

#要想遍历每一个元素，有几维就设几个循环
for j in arr3:
    for p in i:
        for q in p:
            print(q)
#或者使用nditer,输出单个元素
for x in np.nditer(arr3):
    print(x)

#op_dtypes参数来在迭代时更改元素类型，但需要一些空间来进行，所以i传参flags=['buffered']
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#使用不同步长迭代
arrmore=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arrmore[:,::2]):
    print(x)

#进行枚举，序号+内容
for idx,x in np.ndenumerate(arrmore):
    print(idx,x)