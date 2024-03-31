import torch.utils.data
from PIL import Image
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch
import os


class MyDataset(Dataset):
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.transforms = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
        ])
        self.data = []
        for img_filename in os.listdir(image_folder):
            if img_filename.endswith(('.png', '.jpg', '.jpeg')):
                label_filename = img_filename.rsplit('.', 1)[0] + ".txt"
                label_filepath = os.path.join(image_folder, label_filename)
                if os.path.exists(label_filepath):
                    with open(label_filepath, 'r') as f:
                        label = int(f.readline().strip())
                        if label != -1:  # 只添加标签不为-1的数据
                            self.data.append((os.path.join(image_folder, img_filename), label))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image_path, label = self.data[idx]
        image = Image.open(image_path).convert('RGB')
        image = self.transforms(image)
        return image, torch.tensor(label, dtype=torch.long)


ants_image = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\ants_iamge"
ants_test = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\ants_test"
bees_image = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\bees_image"
bees_test = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\bees_test"

# 创建MyDataset实例，加载蚂蚁和蜜蜂图像数据集
ants_dataset = MyDataset(ants_image)
bees_dataset = MyDataset(bees_image)

full_dataset = torch.utils.data.ConcatDataset([ants_dataset, bees_dataset])
train_length = len(full_dataset)

# shuffle=True打乱每次顺序，提高泛化能力
data_loader = DataLoader(full_dataset, batch_size=3, shuffle=True)

# 创建MyDataset实例，加载蚂蚁和蜜蜂测试集图像数据集
ants_test_dataset = MyDataset(ants_test)
bees_test_dataset = MyDataset(bees_test)

# 合并测试集数据集
full_test_dataset = torch.utils.data.ConcatDataset([ants_test_dataset, bees_test_dataset])
test_length = len(full_test_dataset)

# 创建测试集DataLoader
test_data_loader = DataLoader(full_test_dataset, batch_size=3, shuffle=False)


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

learning_rate = 0.01
optimizer = torch.optim.SGD(train_model.parameters(), lr=learning_rate)

total_train_step = 0
total_test_step = 0
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

    # 测试步骤开始
    total_test_loss = 0
    total_accuracy =0

    # 设置模型为评估模式
    train_model.eval()
    # 设置梯度都无，因为只测试
    with torch.no_grad():
        for data in test_data_loader:
            imgs, targets = data
            imgs = imgs.cuda()
            targets = targets.cuda()
            output = train_model(imgs)
            loss = loss_fn(output, targets)
            total_test_loss = total_test_loss + loss.item()
            accuracy = (output.argmax(1) == targets).sum()
            total_accuracy += accuracy

        # 计算平均损失和准确率
        average_test_loss = total_test_loss / len(test_data_loader)
        average_accuracy = total_accuracy / test_length

        print("整体测试集的loss：{}".format(average_test_loss))
        print("整体测试集的准确率：{}".format(average_accuracy))

        # 设置模型回到训练模式
        train_model.train()

        # 保存模型
        torch.save(train_model.state_dict(), "train_bee_ant_{}.pth".format(i + 1))
        print("第 {} 轮模型已保存".format(i + 1))
