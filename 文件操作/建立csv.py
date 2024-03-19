# 现有的数据
existing_data = """
Age,Experience,Rank,Nationality,Go
36,10,9,UK,NO
42,12,4,USA,NO
23,4,6,N,NO
52,4,4,USA,NO
43,21,8,USA,YES
44,14,5,UK,NO
66,3,7,N,YES
35,14,9,UK,YES
52,13,7,N,YES
35,5,9,N,YES
24,3,5,USA,NO
18,3,7,UK,YES
45,9,9,UK,YES
"""

# 将字符串按行分割，并去除空行
lines = existing_data.strip().split("\n")

# 将每行数据拆分为字段，并写入 CSV 文件
with open("shows.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        writer.writerow(line.split(","))

print("CSV 文件已创建成功：shows.csv")
