import torchvision
import torch
from torch import nn

#全局设置，意味着之后所有通过torch.hub下载的内容都会被存储在这个指定的目录下。
torch.hub.set_dir('D:\\Python\\pythonProject1\\learn\\Pytorch')
vgg16_false=torchvision.models.vgg16(pretrained=False)
#从网络中下载训练好的数据集
vgg16_true=torchvision.models.vgg16(pretrained=True)


#在最后添加一个线性层
# vgg16_true.add_module('add_linear',nn.Linear(1000,10))
# print(vgg16_true)

#添加到classifier层级的最后
# vgg16_true.classifier.add_module('add_linear',nn.Linear(1000,10))
# print(vgg16_true)

#修改最后一个线性层
# print(vgg16_false)
# vgg16_false.classifier[6]=nn.Linear(4096,10)
# print(vgg16_false)