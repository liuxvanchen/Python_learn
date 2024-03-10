import os


def batch_rename_files(directory, prefix):
    """
    批量重命名指定目录下的文件，给每个文件名加上前缀。

    参数:
    directory (str): 要重命名文件的目录路径。
    prefix (str): 要添加到文件名前的前缀。
    """
    # 确保目录存在
    if not os.path.isdir(directory):
        print(f"目录 {directory} 不存在。")
        return

        # 遍历目录中的文件
    for filename in os.listdir(directory):
        # 构造文件的完整路径
        file_path = os.path.join(directory, filename)

        # 检查是否为文件（排除目录）
        if os.path.isfile(file_path):
            # 分割文件名和扩展名
            base_name, extension = os.path.splitext(filename)

            # 构造新的文件名
            new_filename = prefix + base_name + extension

            # 构造新的文件完整路径
            new_file_path = os.path.join(directory, new_filename)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f"已将 {filename} 重命名为 {new_filename}")

        # 使用示例


batch_rename_files("C:/Users/Lenovo/Desktop/js/fish-self2/backup_20240310_132249", "new_prefix_")