from torch.utils.data import Dataset
from PIL import Image#导入库
import os#读取文件的库


# 定义一个自定义的数据集类MyData，继承自PyTorch的Dataset类
class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        # 初始化函数，接收两个参数：root_dir（根目录路径）和label_dir（标签目录名）
        self.root_dir = root_dir  # 存储根目录路径
        self.label_dir = label_dir  # 存储标签目录名
        # 拼接根目录和标签目录，得到具体的图片存放路径
        self.path = os.path.join(self.root_dir, self.label_dir)
        # 获取该路径下的所有文件名，作为图片的路径列表
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        # 根据索引获取单个样本的函数
        # 获取文件名
        img_name = self.img_path[idx]
        # 拼接图片完整路径
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        # 使用PIL库打开图片
        img = Image.open(img_item_path)
        # 将标签目录名作为该图片的标签
        label = self.label_dir
        # 返回图片和标签
        return img, label

    def __len__(self):
        # 返回数据集的大小（即图片数量）
        return len(self.img_path)

    # 定义根目录路径


root_dir = "D:\\Python\\pythonProject1\\learn\\Pytorch\\hymenoptera_data\\hymenoptera_data\\train"
# 定义蚂蚁的标签目录名
ants_label_dir = "ants"
# 定义蜜蜂的标签目录名
bees_label_dir = "bees"

# 创建蚂蚁数据集对象
ants_dataset = MyData(root_dir, ants_label_dir)
# 创建蜜蜂数据集对象
bees_dataset = MyData(root_dir, bees_label_dir)

# 尝试将两个数据集相加，但这里会报错，因为PyTorch的Dataset类没有定义__add__方法
# train_dataset = ants_dataset + bees_dataset  # 这一行是错误的，会导致TypeError
