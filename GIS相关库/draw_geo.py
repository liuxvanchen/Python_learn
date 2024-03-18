import geopandas as gpd
import matplotlib.pyplot as plt

# 读取地理数据文件，例如Shapefile
gdf = gpd.read_file('D:/学科资料/地信原理与应用/实验2/实验2数据/china/china.shp')

# 绘制地图
gdf.plot()

# 显示地图
plt.show()