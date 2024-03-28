import torch
import torchvision
from torch.utils.data import DataLoader
from torch import nn
from torch.nn import Linear

dataset_path = "./dataset_CIFAR10"
test_data = torchvision.datasets.CIFAR10(root=dataset_path, train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(test_data, batch_size=64, drop_last=True)


class mylinear(nn.Module):
    def __init__(self):
        super(mylinear, self).__init__()
        self.linear1 = Linear(196608, 10)

    def forward(self, input):
        output = self.linear1(input)
        return output


use_linear = mylinear()
for data in dataloader:
    imgs, tagers = data
    print(imgs.shape)  # torch.Size([16, 3, 32, 32])
    # output = torch.reshape(imgs, (1, 1, 1, -1))  # (样本大小，通道数，H，最后自动计算)
    # 把数据摊平，就是可以不用上面那一行进行一维通道变换，直接输出一个一维数组
    output = torch.flatten(imgs)
    # 使用flatten的话输出就是196608
    print(output.shape)  # torch.Size([1, 1, 1, 49152])这是最后一个，没有进行dorplist的，如果舍去最后几个，所有大小都是196608
    output = use_linear(output)
    print(output.shape)
