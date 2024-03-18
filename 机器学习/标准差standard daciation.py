import numpy
def get_input_numbers():
    # 让用户输入数字，用空格隔开
    input_str = input("请输入一系列数字，用空格隔开：")
    # 将输入的字符串按空格分割，并转换成整数列表
    numbers = list(map(int, input_str.split()))
    return numbers

#求标准差
speed=get_input_numbers()
x=numpy.std(speed)
print(x)

#求方差
x1=numpy.var(speed)
print(x)