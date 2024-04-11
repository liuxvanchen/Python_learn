from osgeo import gdal

# 打开数据集
dataset = gdal.Open('D:\\WeChat\\WeChat Files\\wxid_lvjv33bjbkg222\\FileStorage\\File\\2024-04\\人工林数据\\人工林数据\\人工林郭庆华\\pf20.tif', gdal.GA_ReadOnly)
band = dataset.GetRasterBand(1)

# 定义分块的大小
block_sizes = band.GetBlockSize()
x_block_size = block_sizes[0]
y_block_size = block_sizes[1]

# 获取整个图像的尺寸
xsize = band.XSize
ysize = band.YSize

# 按块读取数据
for y in range(0, ysize, y_block_size):
    if y + y_block_size < ysize:
        rows = y_block_size
    else:
        rows = ysize - y
    for x in range(0, xsize, x_block_size):
        if x + x_block_size < xsize:
            cols = x_block_size
        else:
            cols = xsize - x
        # 读取数据块
        data_array = band.ReadAsArray(x, y, cols, rows)
        # 这里处理你的数据块

# 清理
del band
del dataset
