from numpy import  random
import matplotlib.pyplot as plt
import seaborn as nsn
x=random.logistic(loc=1,scale=2,size=(2,3))
print(x)
nsn.displot(random.logistic(size=1000),kind='kde')
plt.show()

nsn.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
nsn.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()