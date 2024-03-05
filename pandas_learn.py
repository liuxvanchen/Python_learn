import pandas as pd
import matplotlib.pyplot as plt

# 1. 定义输入文件路径
# 对于.xlsx文件
df = pd.read_excel('grade.xlsx', engine='openpyxl')

# 查看缺失值
item=(df.isnull().sum())
print(item)

# 删除含有缺失值的行
df.dropna(inplace=True)

# 删除重复行
df.drop_duplicates(inplace=True)

# 假设'分数'列是字符串类型，转换为整数
df['Score'] = df['Score'].astype(int)

# 筛选出分数大于80分的行
high_scorers = df[df['Score'] > 80]

# 按照分数降序排序
df_sorted = df.sort_values('Score', ascending=False)

# 分组并计算每个班级的平均分
class_average = df.groupby('班级')['Score'].mean()
print(class_average)

# 可视化成绩分布
plt.hist(df['Score'])
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Score Distribution')
plt.show()

# 导出文件
output_file = 'output.xlsx'
df.to_csv(output_file, index=False)
