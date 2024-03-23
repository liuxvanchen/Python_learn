from numpy import random
x=random.randint(100)
print(x)
#random 模块的 rand() 方法返回 0 到 1 之间的随机浮点数。
y=random.rand()
print(y)

x=random.randint(100, size=(5))
print(x)

#生成二维的三行五列
x = random.randint(100, size=(3, 5))
print(x)

#生成三行的2D数组，每行五个随机数
x = random.rand(3, 5)
print(x)