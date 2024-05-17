from functools import reduce


def average(g0, l, gn):
    Va = 1 / 2 * (g0 + gn) * l
    print(f"use average: {Va}")


def half(gh, l):
    Vh = gh * l
    print(f"use half: {Vh}")


def avg_cut(g, L, l):
    # 输入n段每段的横截面积，从小到大
    ll = L - l * (len(g) - 1)  # ll为顶圆锥的高度
    sum = reduce(lambda x, y: x + y, g[1:-1], 0)
    Vac = (g[0] + g[- 1]) / 2 * l + float(sum) * l + 1 / 3 * g[0] * ll
    print(f"use avg_cut: {Vac}")


def half_cut(g, l, L, g0):
    # 输入中点横截面值，l为每段的长度（均分），L为整体长度
    ll = L - l * len(g)  # ll为顶圆锥的高度
    sum = reduce(lambda x, y: x + y, g[:], 0)
    Vhc = float(sum) * l + 1 / 3 * g0 * ll
    print(f"use half_cut: {Vhc}")


def get_input_numbers():
    # 让用户输入数字，用空格隔开
    input_str = input("请输入一系列数字，用空格隔开：")
    # 将输入的字符串按空格分割，并转换成浮点数列表
    numbers = list(map(float, input_str.split()))
    return numbers


# g = get_input_numbers()
g2 = get_input_numbers()
#gh = 0.01307
g0 = 0.000705
# gn = 0.03906#0.04047
l = 5
L = 18.7
#half(gh, L)
# average(g0, L, gn)
half_cut(g2, l, L, g0)
# avg_cut(g, L, l)
# 0.00053 0.00407 0.00849 0.01208 0.01539 0.01863 0.02433 0.03398
# 请输入一系列数字，用空格隔开：0.00053 0.00407 0.00849 0.01208 0.01539 0.01863 0.02433 0.03398
# 请输入一系列数字，用空格隔开：0.00212 0.00636 0.01057 0.01368 0.01674 0.02112 0.02835
#带皮
#0.00196 0.00283 0.00849 0.01267 0.01389 0.01517 0.02351 0.04047
#0.00255 0.00466 0.01094 0.01389 0.01539 0.02011 0.02688
#去皮
#0.00166 0.00246 0.00785 0.01188 0.01307 0.01431 0.02243 0.03906
#0.00221 0.00419 0.01021 0.01307 0.01453 0.01911 0.02573