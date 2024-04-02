import h5py
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

# 打开HDF文件
file_path = 'your_data.hdf5'
with h5py.File(file_path, 'r') as hdf:
    # 假设你知道你需要的数据集的名称
    dataset = hdf['your_dataset_name']
    data = dataset[:]

# 示例：归一化数据
data_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

data_tensor = torch.tensor(data_normalized, dtype=torch.float)


class CustomHDF5Dataset(Dataset):
    def __init__(self, file_path, transform=None):
        self.file_path = file_path
        self.transform = transform
        with h5py.File(self.file_path, 'r') as hdf:
            self.length = len(hdf['your_dataset_name'])

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        with h5py.File(self.file_path, 'r') as hdf:
            data = hdf['your_dataset_name'][idx]
        if self.transform:
            data = self.transform(data)
        return data


# 实例化Dataset
dataset = CustomHDF5Dataset(file_path='your_data.hdf5', transform=torch.tensor)

# 创建DataLoader
data_loader = DataLoader(dataset, batch_size=32, shuffle=True)
