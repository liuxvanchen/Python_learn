import rasterio
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

dataset = rasterio.open('path_to_tiff_file.tiff')
band1 = dataset.read(1)  # 读取第一个波段
band2 = dataset.read(2)  # 读取第二个波段
# 以此类推...
# 例如，对数据进行归一化
band1 = (band1 - band1.min()) / (band1.max() - band1.min())

band1_tensor = torch.from_numpy(band1).float()
band2_tensor = torch.from_numpy(band2).float()
# 如果有更多波段，继续转换
# 假设band1_tensor和band2_tensor都已经被转换为张量
# 张量堆叠，生成一个新的通道，将新生成的通道添加到最前面的维度
stacked_tensor = torch.stack([band1_tensor, band2_tensor], dim=0)


class TiffDataset(Dataset):
    def __init__(self, tiff_path_list):
        self.tiff_path_list = tiff_path_list

    def __len__(self):
        return len(self.tiff_path_list)

    def __getitem__(self, idx):
        with rasterio.open(self.tiff_path_list[idx]) as dataset:
            band_data = [dataset.read(i).astype('float32') for i in range(1, dataset.count + 1)]
            band_data = np.stack(band_data)
            return torch.from_numpy(band_data)


tiff_dataset = TiffDataset(['path_to_tiff1.tiff', 'path_to_tiff2.tiff', ...])
tiff_loader = DataLoader(tiff_dataset, batch_size=4, shuffle=True)
