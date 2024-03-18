import numpy
import matplotlib.pyplot as plt
#用来查看拟合度
from sklearn.metrics import r2_score

def get_input_numbers():
    num=input("enter the numbers with',':")
    numbers=list(map(int,num.split(',')))
    return numbers

hour=get_input_numbers()
speed=get_input_numbers()

#polyfit：numpy提供的多项式模型，3代表是一个三阶的，输入xy，返回多项式的系数
#poly1d：接受多项式各项的系数，返回一个poly1d对象表示多项式
mymodel=numpy.poly1d(numpy.polyfit(hour,speed,3))

#返回一个1到22之间有100个元素的等差数列
myline=numpy.linspace(1,22,100)#从位置1开始，到位置22结束

#绘制原始离散点
plt.scatter(hour,speed)
#画出多项式回归线
plt.plot(myline,mymodel(myline))
plt.show()

#输出拟合度r
print(r2_score(speed,mymodel(hour)))

#用来预测
speed1=mymodel(17)
print(speed1)