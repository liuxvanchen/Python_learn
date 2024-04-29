from osgeo import gdal, osr

# 输入和输出文件
input_file = 'D:\\Python\\pythonProject1\\论文\\forest_new1.tif'
output_file = 'D:\\Python\\pythonProject1\\论文\\forest_new.tif'

# 打开源文件
src = gdal.Open(input_file)

# 源文件的投影信息
src_proj = src.GetProjection()

# 创建输出的坐标参考系统（WGS84）
tgt_proj = osr.SpatialReference()
tgt_proj.ImportFromEPSG(4326)  # WGS84 的 EPSG 代码

# 设置重投影的配置
warp_options = gdal.WarpOptions(dstSRS=tgt_proj)

# 执行重投影
gdal.Warp(output_file, src, options=warp_options)

# 清理
src = None
