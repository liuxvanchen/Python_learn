
#
# # 打开 Shapefile
# driver = ogr.GetDriverByName('ESRI Shapefile')
# data_source = driver.Open('D:\学科资料\地信原理与应用\实验7\实验7\实验7数据\stations.shp', 0)  # 0 表示只读模式
#
# # 获取第一个图层
# layer = data_source.GetLayer()
#
#
# # 遍历图层中的要素
# for feature in layer:
#     geometry = feature.GetGeometryRef()
#     # 这里你可以对 geometry 进行操作，例如获取其坐标、类型等
#     print(geometry.ExportToWkt())  # 输出 Well-Known Text 表示的几何体

# import geopandas as gpd
# import matplotlib.pyplot as plt
# from osgeo import ogr
#
# # 读取SHP文件
# gdf = gpd.read_file('D:\学科资料\地信原理与应用\实验7\实验7\实验7数据\stations.shp')
#
# # 使用geopandas的plot方法显示矢量数据
# gdf.plot()
# plt.title('SHP Vector Data Display')
# plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt

# 读取SHP文件
gdf = gpd.read_file('D:/学科资料/地信原理与应用/实验7/实验7/实验7数据/stations.shp')

# 提取地理坐标
x = gdf.geometry.x
y = gdf.geometry.y

# 绘制图形
plt.figure(figsize=(10, 8))
plt.scatter(x, y, color='red', marker='o', label='Stations')
plt.title('SHP Data Visualization')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.show()
