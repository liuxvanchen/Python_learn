from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#scale - 速率的倒数（参见泊松分布中的 lam）默认为 1.0。
x=random.exponential(scale=2,size=(2,3))
print(x)

sns.displot(random.exponential(size=1000),kind='kde')
plt.show()