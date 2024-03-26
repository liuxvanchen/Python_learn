from torchvision import transforms
from PIL import Image
import cv2
from torch.utils.tensorboard import SummaryWriter

# python的用法》 tensor数据类型
# 通过 transforms.ToTensor去看两个问题
# 1、transforms该如何使用(python)
# 2、为什么我们需要Tensor数据类型

# D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\ants_image\\0013035.jpg
# Pytorch/hymenoptera_data/hymenoptera_data/train/ants_image/0013035.jpg
image_path="D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\ants_image\\5650366_e22b7e1065.jpg"
img = Image.open(image_path)

wirter=SummaryWriter("logs")

# 这一行创建了一个ToTensor对象，该对象是一个转换（transform）函数，用于将PIL图像或NumPy ndarray转换为PyTorch张量（tensor）
tensor_trans = transforms.ToTensor()
# 将img类型的图片转换成tensor类型
tensor_img = tensor_trans(img)
# tensor_img是一个形状为(C, H, W)的浮点数张量，其值在0.0到1.0之间，可以直接用于PyTorch的神经网络模型。
# print(tensor_img)

wirter.add_image("Tensor_img",tensor_img)
wirter.close()


