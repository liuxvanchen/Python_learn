import torchvision
from torch.utils.tensorboard import SummaryWriter

# 可以进行组合操作，这里只有totensor
dataset_tranform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
train_set = torchvision.datasets.CIFAR10(root="./dataset_CIFAR10", train=True, transform=dataset_tranform,
                                         download=True)
test_set = torchvision.datasets.CIFAR10(root="./dataset_CIFAR10", train=False, transform=dataset_tranform,
                                        download=True)

# print(test_set[0])
# img,target=test_set[0]
# #输出图片的信息，如类型和大小
# print(img)
# #输出图片的标签（0-9）
# print(target)
# print(test_set.classes[target])
# img.show()

# print(test_set[0])

# 这里日志名字变了，开tensorboard的时候要注意
writer = SummaryWriter("p10")

for i in range(10):
    img, targer = test_set[i]
    writer.add_image("test_ste", img, i)

writer.close()
