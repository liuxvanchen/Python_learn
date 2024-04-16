from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# 加载图像
img = Image.open('D:\Python\pythonProject1\论文\Forest.tif')
img_array = np.array(img)

# 查看唯一的像素值
unique_values = np.unique(img_array)
print(unique_values)

# 统计标记为1的数量
count_1 = np.sum(img_array == 1)

# 统计标记为3的数量
count_3 = np.sum(img_array == 3)

print(f"标记为1的像素数量: {count_1}")
print(f"标记为3的像素数量: {count_3}")

# #转换之后可以用来检查
# # 统计标记为1的像元数量
# count_1 = (forest_mask_da == 1).sum().item()
# print(f"标记为1的像元数量: {count_1}")
#
# # 统计标记为3的像元数量
# count_3 = (forest_mask_da == 3).sum().item()
# print(f"标记为3的像元数量: {count_3}")


