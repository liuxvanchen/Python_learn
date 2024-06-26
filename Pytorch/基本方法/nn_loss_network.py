import torch
from torch import nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


##这里面的图像处理是瞎写的
class ChuLi(nn.Module):
    def __init__(self):
        super(ChuLi, self).__init__()
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
        # 整合为一个步骤
        x = self.model1(x)
        return x


data_path = "./dataset_CIFAR10"
test_set = torchvision.datasets.CIFAR10(root=data_path, train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(test_set, batch_size=64, drop_last=True)

loss = nn.CrossEntropyLoss()
chuli = ChuLi()
for data in dataloader:
    imgs, targers = data
    output = chuli(imgs)
    result_loss = loss(output, targers)
    result_loss.backward()
    print("ok")
