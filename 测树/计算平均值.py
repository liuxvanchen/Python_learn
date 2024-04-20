import pandas as pd

excel_file = '序号为偶数的数据.xlsx'

# 读取数据
data = pd.read_excel(excel_file)

# 定义胸径和树高的列名
diameter_column = 'R'
height_column = 'H'
j_column = 'n'
v_column='V'

# 获取对应的材积数据
average_v = data.groupby(j_column)[v_column].mean()
formatted_v = average_v.apply(lambda x: f"{x:.3f}")
# 获取对应的胸径数据
average_diameter=data.groupby(j_column)[diameter_column].mean()
formatted_diameter = average_diameter.apply(lambda x: f"{x:.1f}")

# 打印树高数据
print(f"径阶对应的材积数据:")
print(formatted_v)
print("-----------------------")
print(f"径阶对应的胸径数据:")
print(formatted_diameter)
