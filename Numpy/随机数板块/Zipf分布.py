from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#齐夫定律： 在一个集合中，第 n 个常用项是最常用项的 1/n 倍。 例如。 英语中第 5 个常用词的出现次数几乎是最常用词的 1/5。
#a-分布参数
x = random.zipf(a=2, size=(2, 3))

print(x)
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()