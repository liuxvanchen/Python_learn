from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.normal(size=(2,3))
print(x)

#loc表示平均值，scale是标准差（显示图形分布的平整度，size是返回数组的形状
y=random.normal(loc=1,scale=2,size=(2,3))
print(y)

sns.displot(random.normal(size=1000),kind='hist')
plt.show()

