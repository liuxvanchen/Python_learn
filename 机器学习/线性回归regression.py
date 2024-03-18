import matplotlib.pyplot as plt
from scipy import stats


def get_input_number():
    num = input("enter some numbers with',': ")
    numbers = list(map(int, num.split(',')))
    return numbers


x = get_input_number()
y = get_input_number()

slope, intercept, r, p, std_err = stats.linregress(x, y)
# 线性拟合的好坏，r越接近1拟合度越好，xy之间关系好
print(r)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#预测不存在的值
speed=myfunc(10)
print(speed)
