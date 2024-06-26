import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# 从model文件引入所有
from model import *

data_path = "../dataset_CIFAR10"
train_data = torchvision.datasets.CIFAR10(root=data_path, train=True, transform=torchvision.transforms.ToTensor())
test_data = torchvision.datasets.CIFAR10(root=data_path, train=False, transform=torchvision.transforms.ToTensor())

# 获得数据集长度
train_data_size = len(train_data)
test_data_size = len(test_data)

print("训练数据集长度为：{}".format(train_data_size))
print("测试数据集长度为：{}".format(test_data_size))

# 利用dataloader来加载数据集
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

# 搭建神经网络
train_model = Train_model()

# 创建损失函数
loss_fn = nn.CrossEntropyLoss()

# 定义优化器
learning_rate = 0.1  # 单独设置成变量，1e-2
optimizer = torch.optim.SGD(train_model.parameters(), lr=0.01)

# 设置训练网络变量
# 记录训练次数
total_train_step = 0
# 记录测试次数
total_test_step = 0
# 训练轮数
epoch = 10

# 添加tensorboard
writer = SummaryWriter("train_logs")

for i in range(epoch):
    print("--------第 {} 轮训练开始---------".format(i + 1))

    # 训练步骤开始
    for data in train_dataloader:
        imgs, targets = data
        output = train_model(imgs)
        loss = loss_fn(output, targets)

        # 优化器优化模型
        # 梯度清零
        optimizer.zero_grad()
        # 反向传播
        loss.backward()
        # 参数更新
        optimizer.step()

        total_train_step += 1
        # 逢一百打印记录：
        if total_train_step % 100 == 0:
            print("训练次数：{}，Loss：{}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    # 测试步骤开始
    total_test_loss = 0
    # 设置梯度都无，因为只测试
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            output = train_model(imgs)
            loss = loss_fn(output, targets)
            total_test_loss = total_test_loss + loss.item()
            accuracy = (output.argmax(1) == targets).sum()
            toatl_accuracy = toatl_accuracy + accuracy

    print("整体测试集的loss{}".format(total_test_loss))
    print("整体测试集上的正确率：{}".format(toatl_accuracy / test_data_size))
    writer.add_scalar("test_accuracy", toatl_accuracy / test_data_size, total_test_step)
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    total_test_step = total_test_step + 1

    torch.save(train_model, "train_model_{}.pth".format(i))
    print("模型已保存")

writer.close()
