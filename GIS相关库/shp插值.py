import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 读取.shp文件
gdf = gpd.read_file('D:\学科资料\地信原理与应用\实验7\实验7\实验7数据\stations.shp')

# 假设.shp文件中包含'x', 'y', 和'elevation'字段
x = gdf['geometry'].x
y = gdf['geometry'].y
z = gdf['ELEVATION']  # 高程数据

# 创建网格来插值
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# 插值，这里使用线性插值方法，你也可以尝试'cubic'等其他方法linear
zi = griddata((x, y), z, (xi, yi), method='cubic')

# 绘制等高线图
plt.contour(xi, yi, zi, levels=14, linewidths=0.5, colors='k')
plt.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
plt.colorbar(label='Elevation (m)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Elevation Contour Map')
plt.show()
