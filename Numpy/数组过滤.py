import numpy as np
#如果索引处的值为 True，则该元素包含在过滤后的数组中；如果索引处的值为 False，则该元素将从过滤后的数组中排除。
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]
newarr = arr[x]
print(newarr)

filter_arr=[]
for element in arr:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr=arr[filter_arr]
print(filter_arr)
print(newarr)

arr2=np.array([1,2,3,4,5,9,8,12,65,56])
empty=[]
for i in arr2:
    if i%2==0:
        empty.append(True)
    else:
        empty.append(False)
judge=arr2[empty]
print(judge)

#直接过滤
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)