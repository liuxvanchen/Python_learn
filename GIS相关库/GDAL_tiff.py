from osgeo import gdal
import matplotlib.pyplot as plt

# 打开GeoTIFF文件
dataset = gdal.Open('D:\Python\pythonProject1\论文\Forest.tif', gdal.GA_ReadOnly)

# 获取栅格波段的数量
band_count = dataset.RasterCount

# 读取第一个波段的数据
band1 = dataset.GetRasterBand(1)
data = band1.ReadAsArray()

# 获取地理坐标信息
geo_transform = dataset.GetGeoTransform()
minx, px_w, rot1, maxy, rot2, px_h = geo_transform
maxx = minx + dataset.RasterXSize * px_w
miny = maxy + dataset.RasterYSize * px_h

# 使用matplotlib显示图像
plt.imshow(data, cmap='gray')  # 对于单波段图像，通常使用灰度图
# plt.colorbar()  # 显示颜色条
plt.title('TIFF Image Display')
plt.show()

# 打印数据范围
print(f"Data range: ({minx}, {miny}) to ({maxx}, {maxy})")

# 清理资源
band1 = None
dataset = None
