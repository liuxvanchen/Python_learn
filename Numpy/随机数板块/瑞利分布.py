from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#瑞利分布用于信号处理。
#scale -（标准差）决定分布的平坦程度，默认为 1.0）。

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()