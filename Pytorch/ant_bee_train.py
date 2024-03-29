import torch.utils.data
from PIL import Image
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch
import os


class MyDataset(Dataset):
    def __init__(self, image_folder, label_folder):
        self.image_folder = image_folder
        self.label_folder = label_folder
        self.image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if
                            img.endswith(('.png', '.jpg', '.jpeg'))]
        self.transforms = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor()
        ])
        # 类别名称到整数的映射
        self.label_to_int = {'bees': 0, 'ants': 1}  # 根据你的实际标签调整

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image_name = os.path.basename(image_path)
        label_filename = image_name.rsplit('.', 1)[0] + ".txt"
        label_filepath = os.path.join(self.label_folder, label_filename)

        if not os.path.exists(label_filepath):
            print(f"Warning: Label file {label_filepath} not found.")
            label = -1  # 特殊值，表示标签文件缺失
        else:
            with open(label_filepath, 'r') as f:
                label_name = f.readline().strip()
                # 使用映射将类别名称转换为整数
                label = self.label_to_int.get(label_name, -1)  # 如果标签不在映射中，返回-1

        image = Image.open(image_path).convert('RGB')
        image = self.transforms(image)

        return image, torch.tensor(label, dtype=torch.long)


ants_image = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_image"
ants_label = "D:/Python/pythonProject1/learn/Pytorch/dataset/ants_label"
bees_image = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_image"
bees_label = "D:/Python/pythonProject1/learn/Pytorch/dataset/bees_label"
ants_dataset = MyDataset(ants_image, ants_label)
bees_dataset = MyDataset(bees_image, bees_label)

full_dataset = torch.utils.data.ConcatDataset([ants_dataset, bees_dataset])

# shuffle=True打乱每次顺序，提高泛化能力
data_loader = DataLoader(full_dataset, batch_size=32, shuffle=True)


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


train_model = Ant_Bee_Model()
train_model = train_model.cuda()

loss_fn = nn.CrossEntropyLoss()
loss_fn = loss_fn.cuda()

learning_rate = 0.1
optimizer = torch.optim.SGD(train_model.parameters(), lr=learning_rate)

total_train_step = 0
epoch = 10

for i in range(epoch):
    print("--------第 {} 轮训练开始---------".format(i + 1))

    for data in data_loader:
        imgs, targets = data
        imgs = imgs.cuda()
        targets = targets.cuda()
        output = train_model(imgs)
        loss = loss_fn(output, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1

        if total_train_step % 10 == 0:
            print("训练次数：{}，Loss：{}".format(total_train_step, loss.item()))

    torch.save(train_model, "train_bee_ant_{}.pth".format(i))
    print("第 {} 轮模型已保存".format(i + 1))
