import rasterio

with rasterio.open('C:/Users/Lenovo/Desktop/js/lll.tif') as src:
    print(src.meta)  # 打印元数据
    data = src.read(1)  # 读取第一个波段的数据


