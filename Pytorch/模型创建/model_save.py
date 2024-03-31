import torchvision
import torch

vgg16=torchvision.models.vgg16(pretrained=False)

#保存方式1,保存的是模型结构和参数
# torch.save(vgg16,"vgg16_method1.pth")

#保存方式2，保存模型参数（推荐）
torch.save(vgg16.state_dict(),"vgg16_method2.pth")