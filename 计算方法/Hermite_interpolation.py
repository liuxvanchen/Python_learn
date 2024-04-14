def Hermite(x, y, y1, x_inter):
    # 计算 Hermite 插值多项式中的系数 a0
    a0 = (1 + 2 * (x_inter - x[0]) / (x[1] - x[0])) * ((x_inter - x[1]) / (x[0] - x[1])) ** 2
    a1 = (1 + 2 * (x_inter - x[1]) / (x[0] - x[1]))*((x_inter - x[0]) / (x[1] - x[0])) ** 2
    b0 = (x_inter - x[0])*((x_inter - x[1]) / (x[0] - x[1])) ** 2
    b1 = (x_inter - x[1])*((x_inter - x[0]) / (x[1] - x[0])) ** 2
    H3 = y[0] * a0 + y[1] * a1 + y1[0] * b0 + y1[1] * b1
    return H3


x = input("Please enter the x(1,2):")
x_enter = list(map(float, x.split()))
y = input("Please enter the y(1,2):")
y_enter = list(map(float, y.split()))
y1 = input("Please enter the y1(1,2):")
y1_enter = list(map(float,y1.split()))
x_inter = float(input("enter the number you want to guess:"))
result = Hermite(x_enter, y_enter, y1_enter, x_inter)

print(f"the result of Hermite is:{result}")
