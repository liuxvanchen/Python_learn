import math

def calculate_circle_area(diameter_cm):
    # 计算半径（厘米）
    radius_cm = diameter_cm / 2
    # 计算面积（平方厘米）
    area_sq_cm = math.pi * (radius_cm ** 2)
    # 转换面积到平方米
    area_sq_m = area_sq_cm / 10000
    return area_sq_m

def calculate_cone_volume(diameter_cm, height_cm):
    # 计算底面积（平方米）
    base_area_sq_m = calculate_circle_area(diameter_cm)
    # 转换高度到米
    height_m = height_cm / 100
    # 计算体积（立方米）
    volume_cu_m = (1/3) * base_area_sq_m * height_m
    return volume_cu_m

# 输入直径（厘米）
diameter_cm = float(input("请输入圆的直径（厘米）: "))
# 输入高度（厘米）
height_cm = float(input("请输入圆锥的高度（厘米）: "))

# 计算圆锥体积（立方米）
volume_cu_m = calculate_cone_volume(diameter_cm, height_cm)

# 输出结果
print(f"直径为 {diameter_cm} 厘米，高度为 {height_cm} 厘米的圆锥体的体积是 {volume_cu_m:.6f} 立方米")
