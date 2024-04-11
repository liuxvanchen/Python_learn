from osgeo import gdal
import matplotlib.pyplot as plt

# 打开GeoTIFF文件
dataset = gdal.Open('D:\\WeChat\\WeChat Files\\wxid_lvjv33bjbkg222\\FileStorage\\File\\2024-04\\人工林数据\\人工林数据\\人工林郭庆华\\pf20.tif', gdal.GA_ReadOnly)
band = dataset.GetRasterBand(1)

# 确定降采样后的新尺寸
downsample_factor = 4  # 举例减少4倍
new_xsize = band.XSize // downsample_factor
new_ysize = band.YSize // downsample_factor

# 读取数据时降采样
data = band.ReadAsArray(buf_xsize=new_xsize, buf_ysize=new_ysize)

# 使用matplotlib显示图像
plt.imshow(data, cmap='gray')
plt.colorbar()
plt.title('Downsampled TIFF Image Display')
plt.show()
