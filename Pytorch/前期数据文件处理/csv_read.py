import pandas as pd

data = pd.read_csv('your_data.csv')
# 假设每行数据代表一个图像的所有像素
num_images = len(data)
image_size = int(data.shape[1] ** 0.5) # 假设图像是正方形的
images = data.values.reshape(num_images, image_size, image_size)
images = images.astype('float32') / 255.0
images = images[:, None, :, :]  # 在第2维增加通道维度
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        return image, label

# 假设labels是存储在另一个CSV文件中的标签数据
labels = pd.read_csv('your_labels.csv').values

dataset = CustomDataset(images, labels)
data_loader = DataLoader(dataset, batch_size=32, shuffle=True)
