from osgeo import gdal

# 使用原始字符串来处理文件路径
file_path = r'D:\WeChat\WeChat Files\wxid_lvjv33bjbkg222\FileStorage\File\2024-04\人工林数据\人工林数据\人工林郭庆华\pf20.tif'

# 打开GeoTIFF文件
dataset = gdal.Open(file_path, gdal.GA_ReadOnly)

if dataset is None:
    print(f"ERROR: Unable to open file {file_path}")
else:
    # 获取栅格波段的数量
    band_count = dataset.RasterCount

    # 读取第一个波段的数据
    if band_count > 0:
        band = dataset.GetRasterBand(1)
        data = band.ReadAsArray()
        print("Data read successfully.")
    else:
        print("No bands found in dataset.")

    # 清理资源
    dataset = None
