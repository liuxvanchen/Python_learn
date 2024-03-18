#求百分位数
def get_input_nnumbers():
    num=input("请输入一些数字，用逗号隔开")
    numbers=list(map(int,num.split(',')))
    return numbers

import numpy
ages=get_input_nnumbers()
x=numpy.percentile(ages,90)
print(x)