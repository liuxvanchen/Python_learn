# 介绍列表、字典、集合的高级用法
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# 迭代，enumerate获得索引值和元素值
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"Index {index} is {color}")

# 字典推导式
diactory = {y: y ** 2 for y in range(1, 11)}
print(diactory)

# 使用get方法判断字典中是否有该键，没有的话返回None或者指定值
dict_ex = {'name': 'Alice', 'age': 30}
print(dict_ex.get('address', 'No address provided'))
print(dict_ex.get('name'))
print(dict_ex.get('age', 'yes'))#如果是存在的键，会返回该键对应的值

# 集合基本操作，并集，交集，差集，对称差集
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2
print(union_set)

intersection_set = set1 & set2
print(intersection_set)

different_set = set1 - set2
print(different_set)

symmetric_different_set = set1 ^ set2
print(symmetric_different_set)

# 用in来检查集合中的关键字
num_set = {1, 2, 3}
if 2 in num_set:
    print("2 is in the set")

tuple_ex = (1, 'Hello', True)

# tuple_ex[0]=2,因为元组不可以被修改所以这行会报错
# 元组可以作为字典的键
dict_ex = {(1, 'Hello', True): 'value'}
print(dict_ex)

# 也可以作为集合的元素
set_ex = {(1, 'Hello'), (2, 'World')}
print(set_ex)

# 元组解包：从元组中分别提取元素
x, y, z = (1, 'Hello', True)
print(x)
print(y)
print(z)
