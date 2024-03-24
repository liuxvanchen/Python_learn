from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#二项分布是一个离散分布
#参数：试验次数，每次试验发生的概率，生成数组形状
x=random.binomial(n=10,p=0.5,size=(2,3))
print(x)

#画出直方图
sns.displot(random.binomial(n=10,p=0.5,size=1000),kind='hist')
plt.show()

#比较正态分布与二项分布
sns.displot(random.binomial(n=100,p=0.5,size=1000),kind='kde',label='binomial')
sns.displot(random.normal(loc=50,scale=5,size=1000),kind='kde',label='normal')
plt.show()