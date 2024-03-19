import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# 设置种子数，确保每次生成的序列相同
numpy.random.seed(2)

# 正态分布的数据集
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
plt.scatter(x, y)
plt.show()
# 训练集为80%
train_x = x[:80]
train_y = y[:80]
plt.scatter(train_x, train_y)
# mymodel返回一个4阶拟合的多项式
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
# 0-6之间100个值的等差数列
myline = numpy.linspace(0, 6, 100)
plt.scatter(myline, mymodel(myline))
plt.show()

# 测试集为20%
test_x = x[80:]
test_y = y[80:]
plt.scatter(test_x, test_y)
plt.show()

# 判断训练集合拟合度如何，用实际值与多项式拟合值（对train_x进行多项式计算)进行比较看拟合度
r2_1 = r2_score(train_y, mymodel(train_x))
print(r2_1)

# 判断测试集合拟合度如何
r2_2 = r2_score(test_y, mymodel(test_x))
print(r2_2)

# 计算预测值，使用mymodel这个多项式
print(mymodel(5))
