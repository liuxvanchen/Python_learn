from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
# 要读取的图片的绝对路径
image_path = "D:\\Python\\pythonProject1\\learn\\Pytorch\\dataset\\ants_image\\5650366_e22b7e1065.jpg"
# 用PIL打开图片（但是不可用，因为tensorboard读取对类型有要求，详情可以按住ctrl点击add_image
img_PIL = Image.open(image_path)
# 对图片进行类型转换，称为numpy的array
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

# dataformats='HWC':从PIL到numpy，需要在add image()中指定shape中每一个数字/维表示的含义
# test是title，一个title下可以放不同的照片，改变这个数字
# writer.add_image("test",img_array,2,dataformats='HWC')


# 将新的图片添加到 TensorBoard 中，替换之前的图片
writer.add_image("test", img_array, dataformats='HWC')

# y=2x
# for i in range(100):
#     #def add_scalar(self, tag,scalair_value(y轴),global _step（x轴)=None, walltime = None):
#     writer.add_scalar("y=2x",2*i,i)


writer.close()
