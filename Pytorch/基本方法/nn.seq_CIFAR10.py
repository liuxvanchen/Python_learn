import torch
from torch import nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


# 这里面的图像处理是瞎写的
class ChuLi(nn.Module):
    def __init__(self):
        super(ChuLi, self).__init__()
        # self.conv1 = Conv2d(3, 32, 5, padding=2, stride=1)
        # self.maxpool = MaxPool2d(kernel_size=2)
        # self.conv2 = Conv2d(32, 32, 5, stride=1, padding=2)
        # self.maxpool2 = MaxPool2d(kernel_size=2)
        # self.conv3 = Conv2d(32, 64, kernel_size=5, padding=2, stride=1)
        # self.maxpool3 = MaxPool2d(kernel_size=2)
        # self.flatten = Flatten()
        # self.Linear1 = Linear(1024, 64)
        # self.Linear2 = Linear(64, 10)
        # 使用sequential来整合为一个步骤
        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2, stride=1),
            MaxPool2d(kernel_size=2),
            Conv2d(32, 32, 5, stride=1, padding=2),
            MaxPool2d(kernel_size=2),
            Conv2d(32, 64, kernel_size=5, padding=2, stride=1),
            MaxPool2d(kernel_size=2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, x):
        # x=self.conv1(x)
        # x=self.maxpool(x)
        # x=self.conv2(x)
        # x=self.maxpool2(x)
        # x=self.conv3(x)
        # x=self.maxpool3(x)
        # x=self.flatten(x)
        # x=self.Linear1(x)
        # x=self.Linear2(x)
        # 整合为一个步骤
        x = self.model1(x)
        return x


chuli = ChuLi()
# 样本，通道，高，宽
intput = torch.ones((64, 3, 32, 32))
output = chuli(intput)
print(output.shape)

data_path = "./dataset_CIFAR10"
test_set = torchvision.datasets.CIFAR10(root=data_path, train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(test_set, batch_size=64, drop_last=True)

writer = SummaryWriter("sequential_log")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("iniput_seq", imgs, step)
    output = chuli(imgs)
    # 因为chuli最后得到的是一个（64，10）的，要改变一下形状，但是这种并不常用于处理图像
    output = output.reshape((64, 1, 1, 10))
    writer.add_images("output_seq", output, step)
    step = step + 1

writer.add_graph(chuli, intput)
writer.close()
