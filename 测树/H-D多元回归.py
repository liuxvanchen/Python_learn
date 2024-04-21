import numpy as np
import matplotlib.pyplot as plt
# 用来查看拟合度
from sklearn.metrics import r2_score

x = np.array([8.7, 12.3, 16.4, 19.7, 22.8, 26.9, 32.8, 36.5, 42.1])
#树高
# y = np.array([10.6, 14.0, 17.0, 19.3, 20.7, 21.6, 23.2, 24.0, 28.1])
#材积
y=np.array([ 0.034,0.090,0.175,0.274,0.376,0.556,0.831,1.101,1.477])
weights = np.array([9, 19, 11, 9, 3, 2, 3, 1, 1])
x_test = np.array([10.3, 12.8, 15.8, 19.2, 19.8, 22.5, 27.6, 26.0, 24.4])
#树高
#y_test = np.array([8.2, 11.8, 15.7, 20.6, 24.0, 28.9, 33.0, 41.5, 43.5])
#材积
y_test=np.array([0.032,0.073,0.149,0.298,0.403,0.666,1.095,1.125,1.374])
xx=np.array([8,12,16,20,24,28,32,36,40])

def mean_relative_error(y_true, y_pred):
    n = len(y_true)
    mre = np.mean(np.abs((y_true - y_pred) / y))
    return mre

# polyfit：numpy提供的多项式模型，3代表是一个三阶的，输入xy，返回多项式的系数
# poly1d：接受多项式各项的系数，返回一个poly1d对象表示多项式
mymodel = np.poly1d(np.polyfit(x, y, 5))
print(mymodel)

plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']

plt.scatter(x, y, label='数据')

myline = np.linspace(4, 48, 12)  # 从位置4开始，到位置48结束

# 绘制原始离散点
plt.scatter(x, y)
# 画出多项式回归线
plt.plot(myline, mymodel(myline))
plt.title('材积-胸径多项式拟合（五次）')
plt.show()

# 输出拟合度r
print(r2_score(y_test, mymodel(x_test)))
# 使用模型预测测试数据
y_pred_test = mymodel(x_test)

# # 计算测试数据的MRE
# mre_test = mean_relative_error(y_test, y_pred_test)
# print(f"测试数据的MRE: {mre_test}")

yy=mymodel(xx)
print(yy)

