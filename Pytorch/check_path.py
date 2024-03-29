import os

def check_path_exists(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
    else:
        print(f"The path {path} does not exist.")

# 检查图像和标签路径
ants_image = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_image"
ants_label = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_label"
bees_image = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_image"
bees_label = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_label"

check_path_exists(ants_image)
check_path_exists(ants_label)
check_path_exists(bees_image)
check_path_exists(bees_label)


# 打印当前工作目录
current_working_directory = os.getcwd()
print("当前工作目录是:", current_working_directory)

