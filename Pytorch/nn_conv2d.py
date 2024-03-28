import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.nn import Conv2d
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root="./dataset_CIFAR10", train=False,
                                       transform=torchvision.transforms.ToTensor(),
                                       download=True)
dataloader = DataLoader(dataset, batch_size=64)


class JuanJi(nn.Module):
    def __init__(self):
        super(JuanJi, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        #将x放到卷积层中
        x = self.conv1(x)
        return x

#初始化
juanji = JuanJi()
print(juanji)
#Conv2d(3, 6, kernel_size=(3, 3), stride=(1, 1)):
# 表示 conv1 是一个二维卷积层 (Conv2d)，它的输入通道数为 3，输出通道数为 6，
# 卷积核的大小为 3x3，卷积操作的步长为 (1, 1)。

writer=SummaryWriter("conv2d_log")
step=0
for data in dataloader:
    imgs,targets=data
    output=juanji(imgs)
    #print(output.shape)
    print(imgs.shape)#torch.Size([64, 3, 32, 32])
    print(output.shape)#torch.Size([64, 6, 30, 30])通道数量变多，图片变小
    writer.add_images("input",imgs,step)

    #将output进行一个reshape，-1指的是不知道多少但是自动生成
    output=torch.reshape(output,(-1,3,30,30))
    writer.add_images("output",output,step)

    step=step+1

    writer.close()