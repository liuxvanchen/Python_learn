import torch
import torchvision

#方法一
model=torch.load("vgg16_method1.pth")
# print(model)

#方式2加载,保存的是一个字典形式，不是网络模型
model=torch.load("vgg16_method2.pth")
#恢复成网络模型
vgg16=torchvision.models.vgg16(pretrained=False)
#将加载的模型参数字典加载到了空白模型中
vgg16.load_state_dict(torch.load("vgg16_method2.pth"))
print(model)