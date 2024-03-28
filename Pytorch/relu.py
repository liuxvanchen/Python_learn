import torch
import torchvision
from torch import nn
from torch.nn import ReLU
from torch.nn import Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# ReLU就是在元素和0之间取大

input = torch.tensor([[1, -0.5],
                      [-1, 3]])

output = torch.reshape(input, (-1, 1, 2, 2))
print(output.shape)

data_path = "./dataset_CIFAR10"
test_data = torchvision.datasets.CIFAR10(root=data_path, train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(test_data, batch_size=64)


class MyReLu(nn.Module):
    def __init__(self):
        # 实现父类的方法
        super(MyReLu, self).__init__()
        self.relu1 = ReLU()
        self.sigmoid1 = Sigmoid()

    def forward(self, input):
        output = self.sigmoid1(input)
        return output


# 创建的relu类
# relu_tset = MyReLu()
mysigmoid = MyReLu()
# 测试relu的数组的数据
# output = relu_tset(input)
# print(output)

writer = SummaryWriter("sigmoid_log")
step = 0
for data in dataloader:
    imgs, targers = data
    writer.add_images("input_sigmoid", imgs, step)
    # 这里使用mysigmoid类里面的方法，有relu和sigmoid但是因为forward传递出来的只有sigmoid的操作
    output = mysigmoid(imgs)
    writer.add_images("output_sigmoid", output, step)
    step = step + 1

writer.close()
