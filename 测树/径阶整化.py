import pandas as pd

# 读取Excel文件
excel_file = "实验3和实验4 数据.xlsx"

# 指定要读取的列
list1 = ['No']
r1 = ['R']
h1 = ['H']

# 使用pandas读取Excel文件
list_data = pd.read_excel(excel_file, usecols=list1)
r_data = pd.read_excel(excel_file, usecols=r1)
h_data = pd.read_excel(excel_file, usecols=h1)

# 初始化的空列表
diameter_classes = []

# 遍历 R 列的数据并计算 i 列的值
for data in r_data['R']:
    diameter_class = ((data + 2) // 4) * 4
    if diameter_class < 4:
        diameter_class = 4
    diameter_classes.append(diameter_class)

# 将 i 列添加到 DataFrame 中
list_data['径阶'] = diameter_classes

# 将结果写入Excel文件
list_data.to_excel(excel_file, index=False)

