import numpy as np
import matplotlib.pyplot as plt

# 生成一些数据点
x = np.linspace(-10, 10, 50)  # 生成50个x值，范围从-10到10
y = 1.5*x**2 - 10*x + 3  # 使用二次函数生成y值
noise = np.random.normal(0, 20, y.shape)  # 添加一些噪声
y += noise  # 带噪声的数据点

# 使用numpy的polyfit函数进行多项式拟合，这里使用2代表二次多项式
coefficients = np.polyfit(x, y, 2)
polynomial = np.poly1d(coefficients)

# 打印出多项式方程
print("拟合的多项式方程:")
print(polynomial)

# 在同一个图中绘制原始数据和拟合的曲线
plt.figure(figsize=(10, 5))
plt.scatter(x, y, label='Original data', color='blue')  # 绘制原始数据点
plt.plot(x, polynomial(x), label='Fitted polynomial', color='red')  # 绘制拟合的多项式曲线
plt.legend()
plt.title('最佳平方逼近')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
