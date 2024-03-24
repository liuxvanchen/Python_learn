from numpy import  random
import matplotlib.pyplot as plt
import seaborn as sns

#lam为发生概率或者已知次数
x=random.poisson(lam=2,size=10)
print(x)

sns.displot(x,kde=False)
plt.show()