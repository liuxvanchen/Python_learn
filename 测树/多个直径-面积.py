import math

def calculate_circle_area(diameter_cm):
    # 计算半径（厘米）
    radius_cm = diameter_cm / 2
    # 计算面积（平方厘米）
    area_sq_cm = math.pi * (radius_cm ** 2)
    # 转换面积到平方米
    area_sq_m = area_sq_cm / 10000
    return area_sq_m

# 输入多个直径（厘米），使用逗号分隔
diameters_input = input("请输入多个圆的直径（厘米），使用逗号分隔: ")

# 将输入的直径字符串分割成列表，并转换为浮点数
diameters_cm = [float(d) for d in diameters_input.split(',')]

# 计算每个直径对应的面积（平方米）
areas_sq_m = [calculate_circle_area(d) for d in diameters_cm]

# 输出结果
for diameter, area in zip(diameters_cm, areas_sq_m):
    print(f"直径为 {diameter} 厘米的圆的面积是 {area:.6f} 平方米")
#0.043300 0.035783  0.027744 0.023861 0.019669 0.013706 0.005843 0.000705
#0.019943 0.035783 0.019016 0.016742 0.014219 0.011786 0.009931 0.007201 0.005675 0.002767 0.000654 0.000129