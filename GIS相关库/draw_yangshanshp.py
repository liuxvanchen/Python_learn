import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd

# # 创建一个地图图像和轴
# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#
# # 添加自然地理特征
# ax.add_feature(cfeature.LAND)
# ax.add_feature(cfeature.OCEAN)
# ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.BORDERS, linestyle=':')


# 创建一个地图图像和轴
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# 添加自然地理特征
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.LAND, facecolor='gray')

# 设置地图范围（如果需要）
ax.set_extent([70.0, 137.0, 0.0, 55.0], crs=ccrs.PlateCarree())

# 绘制你的数据或者其他地图元素...

# 设置地图范围（如果需要）
ax.set_extent([70.0, 137.0, 0.0, 55.0], crs=ccrs.PlateCarree())

# 读取Shapefile文件并转换为PlateCarree投影
gdf = gpd.read_file('D:/学科资料/地信原理与应用/实验2/实验2数据/china/china.shp')
gdf = gdf.to_crs(ccrs.PlateCarree().proj4_init)

# 绘制北京的边界
gdf.plot(ax=ax, edgecolor='red', facecolor='none')

plt.show()
