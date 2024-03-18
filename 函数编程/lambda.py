add = lambda x, y: x + y
print(add(8, 9))

numbaers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
event_numbers = list(filter(lambda x: x % 2 == 0, numbaers))
print(event_numbers)

# sorted用法：要排序的，key=一个函数，reverse=Ture为降序（默认是升序）
words = ['apple', 'banana', 'pear', 'cherry']
# 这里接受了一个lambda函数来返回words里面的每个元素的长度，word只是一个参数，名字不影响，只是告诉前面这是一个计算长度的函数
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)

#map是一个可以用于迭代的，接受想要作用于元素的函数和元素列表
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
