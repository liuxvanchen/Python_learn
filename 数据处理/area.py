import math
def get_input_numbers():
    # 让用户输入数字，用空格隔开
    input_str = input("请输入一系列数字，用空格隔开：")
    # 将输入的字符串按空格分割，并转换成浮点数列表
    numbers = list(map(float, input_str.split()))
    return numbers

def area(d):
    areas = [math.pi/4*(di*0.01)**2 for di in d]
    for i, area in enumerate(areas):
        print(f"第{i + 1}个圆的面积：{area:.5f}")


d=get_input_numbers()
area(d)
