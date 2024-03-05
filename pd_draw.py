import pandas as pd
import matplotlib.pyplot as plt

# 读取.xlsx文件
file_path = 'grade.xlsx'  # 修改为你的.xlsx文件路径
df = pd.read_excel(file_path, engine='openpyxl')

# 确保数据是正确的，并且列名是'姓名'和'成绩'
print(df.head())

# 设置图形的大小
plt.figure(figsize=(10, 6))

# 创建条形图
plt.bar(df['Name'], df['Score'], color='b')

# 添加标题和轴标签
plt.title('姓名-成绩图')
plt.xlabel('姓名')
plt.ylabel('成绩')

# 显示图形
plt.xticks(rotation=45)  # 如果姓名太长可以旋转它们以避免重叠
plt.show()