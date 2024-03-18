import matplotlib.pyplot as plt
import numpy
def get_input_number():
    num=input("enter some numbers with',': ")
    numbers=list(map(int,num.split(',')))
    return numbers

# x=get_input_number()
# y=get_input_number()
# #xy的数量要一致，表示横纵坐标
# plt.scatter(x,y)
# plt.show()

x1=numpy.random.normal(5.0,1.0,10000)
y1=numpy.random.normal(10.0,2.0,10000)
plt.scatter(x1,y1)
plt.show()