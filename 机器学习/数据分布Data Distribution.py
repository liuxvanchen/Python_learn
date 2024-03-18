import numpy
import matplotlib.pyplot as plt
#随机生成0-5之间的250个数的列表
x=numpy.random.uniform(0.0,5.0,10000)
plt.hist(x,100)
plt.show()
print(x)