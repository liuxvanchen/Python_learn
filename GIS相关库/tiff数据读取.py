from osgeo import gdal

# 打开TIFF文件
dataset = gdal.Open('D:\\WeChat\\WeChat Files\\wxid_lvjv33bjbkg222\\FileStorage\\File\\2024-04\\人工林数据\\人工林数据\\人工林郭庆华\\pf20.tif')

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
