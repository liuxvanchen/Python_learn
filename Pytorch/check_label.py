import os

def verify_labels_exist(image_dir, label_dir):
    # 遍历图片目录中的所有文件
    for image_name in os.listdir(image_dir):
        # 构建标签文件名（假设图片和标签文件名前缀相同，扩展名不同）
        base_name = os.path.splitext(image_name)[0]  # 移除扩展名
        label_name = base_name + ".txt"  # 构建标签文件名
        label_path = os.path.join(label_dir, label_name)  # 构建标签文件的完整路径

        # 检查标签文件是否存在
        if os.path.exists(label_path):
            print(f"Label file {label_path} for image {image_name} exists.")
        else:
            print(f"Label file {label_path} for image {image_name} does not exist. Please check.")

# 图片和标签目录的路径
ants_image_dir = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_image"
ants_label_dir = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_label"
bees_image_dir = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_image"
bees_label_dir = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_label"

# 对蚂蚁和蜜蜂的图片和标签进行验证
verify_labels_exist(ants_image_dir, ants_label_dir)
verify_labels_exist(bees_image_dir, bees_label_dir)
