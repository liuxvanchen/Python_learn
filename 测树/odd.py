import pandas as pd

# 读取Excel文件
excel_file = "实验3和实验4 数据.xlsx"

# 使用pandas读取Excel文件
data = pd.read_excel(excel_file)

# 筛选序号为单数的所有数据
filtered_data = data[data['No'] % 2 == 0]

# 将筛选后的数据写入新的 Excel 文件
output_file = "序号为偶数的数据.xlsx"
filtered_data.to_excel(output_file, index=False)

print("筛选后的数据已写入Excel文件:", output_file)

