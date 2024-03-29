import os

# 定义你的图片文件夹路径
ants_image_path = 'D:/Python/pythonProject1/learn/Pytorch/dataset/ants_image'
bees_image_path = 'D:/Python/pythonProject1/learn/Pytorch/dataset/bees_image'

# 定义函数来生成标签文件
def generate_label_files(image_folder, label):
    for image_file in os.listdir(image_folder):
        # 只处理图片文件（这里假设是jpg格式的图片）
        if image_file.endswith('.jpg'):
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(image_folder, label_file)
            # 写入标签
            with open(label_path, 'w') as file:
                file.write(str(label))

# 为蚂蚁和蜜蜂图片生成标签文件
generate_label_files(ants_image_path, 0)  # 0代表蚂蚁
generate_label_files(bees_image_path, 1)  # 1代表蜜蜂
