import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])#从第二个到第六个
#注意这里的4是索引值为4.并不是第四个元素，是第五个元素
print(arr[4:])
print(arr[:4])
#负裁切
print(arr[3:-1])
#step来确定步长
print(arr[1:5:2])
#返回数组中相隔的元素
print(arr[::2])

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
#返回第二个元素（第二个方括号）中索引1-4的元素
print(arr2[1,1:4])
#返回两个元素（两个方括号0：2不包括2）中每个的索引为2的元素
print(arr2[0:2, 2])
#返回每个中索引1-3的
print(arr2[0:2,1:3])