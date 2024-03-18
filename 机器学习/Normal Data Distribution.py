import numpy
import matplotlib.pyplot as plt
#正态分布及画图
x=numpy.random.normal(0.0,1.0,10000)#平均值（中轴线的位置），标准差（很少与平均值偏离1）
plt.hist(x,100)
plt.show()