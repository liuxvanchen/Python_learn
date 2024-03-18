import numpy as np

# 假设矩阵的元素是以空格分隔
matrix = np.loadtxt('matrix.txt', delimiter=' ')

# 如果元素是以逗号分隔，请这样做
# matrix = np.loadtxt('matrix.txt', delimiter=',')

print(matrix)

#手动输入
rows = int(input("请输入矩阵的行数："))
matrix = []
for _ in range(rows):
    row = input("请输入矩阵的一行，元素之间以空格分隔：")
    matrix.append([float(num) for num in row.split()])

matrix = np.array(matrix)
print(matrix)

import pandas as pd


# 读取CSV文件
df = pd.read_csv('matrix.csv')

# 如果是Excel文件
# df = pd.read_excel('matrix.xlsx')

matrix = df.values
print(matrix)

