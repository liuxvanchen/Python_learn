import os

# 根目录路径
root_dir = "D:\\Python\\pythonProject1\\learn\\Pytorch\\hymenoptera_data\\hymenoptera_data\\train"

# 目标文件夹名称
target_dir = "ants_image"

# 获取目标文件夹下的所有图像文件名列表
img_path = os.listdir(os.path.join(root_dir, target_dir))

# 提取标签，即目标文件夹名称中的"ants"
label = target_dir.split('_')[0]

# 输出文件夹名称，用于保存标签文件
out_dir = "ants_label"

# 遍历目标文件夹下的每张图像
for i in img_path:
    # 提取文件名（去除后缀名）
    file_name = i.split('.jpg')[0]

    # 构建标签文件的路径，并打开文件进行写入
    with open(os.path.join(root_dir, out_dir, "{}.txt".format(file_name)), 'w') as f:
        # 将标签写入文件
        f.write(label)

