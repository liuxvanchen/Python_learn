from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#遵循帕累托定律的分布，即 80-20 分布（20% 的因素导致 80% 的结果）。
#a - 形状参数。

x = random.pareto(a=2, size=(2, 3))
print(x)
sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()