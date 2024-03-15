import geopandas as gpd

gdf=gpd.read_file('D:/学科资料/地信原理与应用/实验1/实验1/实验1数据/landuse.shp')
# 查看数据的描述性统计信息
gdf.describe()
# 查看数据的空间范围
print(gdf.bounds)
print(gdf.total_bounds)
# 简单的数据可视化
gdf.plot()

# 创建一个缓冲区（例如，每个要素周围200m的区域）
gdf['area']=gdf.area
gdf_buffer=gdf.buffer(200)

# 空间连接（例如，查找与特定多边形相交的所有其他多边形）
# 假设 gdf2 是另一个 GeoDataFrame
joined_gdf=gpd.sjoin(gdf,gdf2,how="inner",op='intersects')