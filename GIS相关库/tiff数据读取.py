from osgeo import gdal

# 打开TIFF文件
dataset = gdal.Open('D:\\Python\\pythonProject1\\论文\\forest_new.tif')

# 获取地理变换信息
geotransform = dataset.GetGeoTransform()

# 分辨率（像素大小）
x_res = geotransform[1]
y_res = geotransform[5]

# 投影信息
projection = dataset.GetProjection()

print(f"X Resolution: {x_res}")
print(f"Y Resolution: {abs(y_res)}")  # 取绝对值，因为y分辨率可能是负数
print(f"Projection: {projection}")
