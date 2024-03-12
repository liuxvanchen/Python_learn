from collections import defaultdict

#使用sort直接对源列表进行更改
my_list=[5,3,1,4,2]
my_list.sort()
print(my_list)

#sorted可以返回一个新列表
sorted_list=sorted(my_list)
print(sorted_list)

#切片用法，不包含3
subset=my_list[1:3]
print(subset)

my_list[1:3]=8,9
print(my_list)

#defaultdict创建一个有默认值的字典
count_dict=defaultdict(int)#创建字典用于计数
for item in ['apple','banana','pear','banana','apple','apple']:
    count_dict[item]+=1
print(count_dict)

#使用字典推导式创建新字典
original_dict={'a':1,'b':3,'c':9}
filtered_dict={k:v for k,v in original_dict.items() if v>2}
print(filtered_dict)

#使用collections模块中的namedtuple函数可以创建具有字段名的元组子类，这使得元组中的元素更易于访问和理解。
from  collections import namedtuple
point=namedtuple('point',['x','y'])
p=point(1,2)
print(p.x)
print(p.y)
