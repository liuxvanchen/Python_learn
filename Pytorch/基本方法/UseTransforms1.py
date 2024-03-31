from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

write = SummaryWriter("logs")
img = Image.open("D:\Python\pythonProject1\learn\基础练习题\DSC00757.JPG")
print(img)

# 使用Totensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
# 将经过 transforms.ToTensor() 转换的图像 img_tensor 添加到 TensorBoard 中，标题为 "Totensor"。
write.add_image("Totensor", img_tensor)


print(img_tensor[0][0][0])
# Normalize(传入每个通道的均值和标准差
trans_norm = transforms.Normalize([1, 3, 5], [3, 2, 0.5])
# 这里传入的img_tensor：先将图像转换为 Tensor 格式，然后进行归一化操作
img_norm = trans_norm(img_tensor)
print(img_tensor[0][0][0])
write.add_image("Normalize", img_norm)

# Resize
# 输入一个PIL的image
print(img.size)
trans_resize = transforms.Resize((512, 512))
# img PIL->使用 resize->img_resize PIL
img_resize = trans_resize(img)
# img_resize-> 使用 trans_totensor ->img_resize tensor
# 同名结果进行覆盖
img_resize = trans_totensor(img_resize)
write.add_image("Resize", img_resize, 0)
print(img_resize)  # 这里输出的是一个tensor类型

# Compose
trans_resize_2 = transforms.Resize((800, 800))
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
img_resize_2 = trans_compose(img)
write.add_image("Resize", img_resize_2, 1)

# RandomCrop
trans_random = transforms.RandomCrop(512)  # 这里可以定义大小（（200，100））
trans_compose_2 = transforms.Compose([trans_random, trans_totensor])
# 循环10次，以便生成10个随机裁剪的图像。
for i in range(10):
    # 使用组合的变换操作将随机裁剪和张量转换应用于原始图像 img，得到裁剪后的图像 img_crop。
    img_crop = trans_compose_2(img)
    # 将裁剪后的图像 img_crop 记录到 TensorBoard 中，标题为 "RandCorp"，并使用 i 作为记录的步数或时间戳，以便在 TensorBoard 中区分不同记录之间的时间关系或顺序关系。
    write.add_image("RandCorp", img_crop, i)

write.close()
