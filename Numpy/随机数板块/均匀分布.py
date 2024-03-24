from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#数据上下限默认为0和1
x = random.uniform(size=(2, 3))

print(x)
sns.displot(random.uniform(size=1000),kind='kde')
plt.show()