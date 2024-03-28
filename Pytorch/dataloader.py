import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# 这一步是将数据集全部转换为tensor格式
test_data = torchvision.datasets.CIFAR10(root="./dataset_CIFAR10", train=False,transform=torchvision.transforms.ToTensor())
# 处理的是tensor格式的data，相当于四张一组,最后一个参数看是否舍去（True舍去余数
teat_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=False)

# 测试数据集第一张样本图片及target
img, target = test_data[0]
print(img.shape)  # 图片RGB通道和大小
print(target)  # 属于什么类别

writer = SummaryWriter("dataloader")
#看循环两轮，并且把shuffle=True，打乱顺序
for epoch in range(2):
    step = 0
    for data in teat_loader:
        imgs, targets = data
        # 都是四张，所有都有四个参数
        # print(imgs.shape)
        # print(targets)

        #注意这里是add_images!
        writer.add_images("epoch:{}".format(epoch), imgs, step)
        #  imgs = imgs.permute(0, 3, 1, 2)  # 将通道维度从最后一维调整到第2维
        #  writer.add_image("test_data", imgs, step, dataformats='CHW')  # 设置 dataformats='CHW'
        step = step + 1

writer.close()
