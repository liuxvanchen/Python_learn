import os


# 检查是否都对应了文件和标签
def check_label_exists(image_folder):
    missing_labels = []
    for img_filename in os.listdir(image_folder):
        if img_filename.endswith(('.png', '.jpg', '.jpeg')):
            label_filename = img_filename.rsplit('.', 1)[0] + ".txt"
            label_filepath = os.path.join(image_folder, label_filename)
            if not os.path.exists(label_filepath):
                missing_labels.append(img_filename)
    return missing_labels


# 使用示例
ants_image = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\bees_image"
missing_labels = check_label_exists(ants_image)
if len(missing_labels) > 0:
    print("以下图片缺少对应的标签文件:")
    for filename in missing_labels:
        print(filename)
else:
    print("所有图片均有对应的标签文件。")
