import torch
import torchvision
from PIL import Image
from torch import nn

img_path = "D:\\Python\\pythonProject1\\learn\\Pytorch\\imgs\\bee2.png"
image = Image.open(img_path)
print(image)
image = image.convert('RGB')

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])

image = transform(image)
print(image.shape)
if torch.cuda.is_available():
    image = image.cuda()

class Ant_Bee_Model(nn.Module):
    def __init__(self):
        super(Ant_Bee_Model, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Flatten(),
            nn.Linear(in_features=64 * 4 * 4, out_features=64),
            nn.Linear(in_features=64, out_features=2)
        )

    def forward(self, x):
        x = self.model(x)
        return x


# 创建模型对象
model = Ant_Bee_Model()

# 加载模型参数
checkpoint_path = "train_bee_ant_6.pth"
checkpoint = torch.load(checkpoint_path)
model.load_state_dict(checkpoint)

# 将模型移动到GPU（如果可用）
if torch.cuda.is_available():
    model = model.cuda()

# 调用模型进行推理
image = torch.reshape(image, (1, 3, 32, 32))
model.eval()
with torch.no_grad():
    output = model(image)
    print(output)

# 处理模型输出
predicted_label = torch.argmax(output, dim=1).item()
class_labels = ['ant', 'bee']
predicted_label_name = class_labels[predicted_label]

# 打印预测结果
print("预测的类别标签为:", predicted_label_name)
