import os
import random
import matplotlib.pyplot as plt

import numpy

with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

    for line in f:
        print(line)

with open('file2.txt', 'w') as f2:
    f2.write('this is additional content.\n')

# 获取当前工作目录
current_dir = os.getcwd()
print("current directory:", current_dir)

# 列出指定目录下的所有文件
files = os.listdir(current_dir)
print("File in current direcotry:", files)

# 检查文件是否存在

file_exists = os.path.exists('file.txt')
print("file exists:", file_exists)

# 获取文件大小（字节数）

file_size = os.path.getsize('file.txt')
print("file size:", file_size, "bytes")



