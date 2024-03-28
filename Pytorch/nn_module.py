import torch
from torch import nn

class My_Nn(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output

# 实例化模型
liushen = My_Nn()

# 定义输入数据
x = torch.tensor([1])

# 将输入数据传递给模型的 forward 方法
output = liushen(x)

print(output)
