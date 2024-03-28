import torch
from torch import nn
from torch.nn import MaxPool2d
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# input = torch.tensor([[1, 2, 0, 3, 1],
#                       [0, 1, 2, 3, 1],
#                       [1, 2, 1, 0, 0],
#                       [5, 2, 3, 1, 1],
#                       [5, 1, 0, 1, 1]], dtype=torch.float32)
# # 这里使用dtype是把元素改成float
#
# input = torch.reshape(input, (-1, 1, 5, 5))
# print(input.shape)

# 上图片...
dataset_path = "./dataset_CIFAR10"
test_data = torchvision.datasets.CIFAR10(root=dataset_path, train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(test_data, batch_size=64)


class MaxPool(nn.Module):
    def __init__(self):
        super(MaxPool, self).__init__()
        self.maxpool = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool(input)
        return output


# 这里是上面矩阵的验证
max = MaxPool()
# output = max(input)
# print(output)

writer = SummaryWriter("maxpool_log")
step = 0

for data in dataloader:
    imgs, targets = data
    writer.add_images("input_pool", imgs, step)
    # 这里的max是上面类的实例化
    output = max(imgs)
    writer.add_images("output_pool", output, step)
    step = step + 1

writer.close()
