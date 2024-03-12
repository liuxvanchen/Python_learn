numbers = [1, 2, 3, 4, 5]
numbers2 = [4, 5, 6, 7, 8]
squared = map(lambda x: x ** 2, numbers)
add = map(lambda x1, x2: x1 + x2, numbers, numbers2)
print(list(squared))
print(list(add))
