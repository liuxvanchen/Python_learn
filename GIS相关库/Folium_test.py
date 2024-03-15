import folium
from folium.plugins import HeatMap

# 创建一个地图对象
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
folium.Marker([40.7128, -74.0060], popup='New York City').add_to(m)

# 定义一个可缩放的圆形标记，使用地理坐标单位（如米）来设置半径
# 假设我们想要半径为500米的圆
circle = folium.Circle(
    location=[40.7128, -74.0060],  # 中心点坐标
    radius=500,  # 半径，单位是米
    popup='Central Park',  # 弹出框文本
    color='red',  # 圆的颜色
    fill=True,  # 是否填充圆内部
    fill_color='rgba(255, 0, 0, 0.3)',  # 填充颜色，可以是rgba格式以设置透明度
    fill_opacity=0.5  # 填充颜色的透明度
).add_to(m)
# 在这个例子中，radius=500意味着圆的半径是500米。由于这是基于地理坐标单位的，所以当用户缩放地图时，圆的大小会根据当前视图的比例尺自动调整。圆的边缘将始终代表距离中心点500米的范围。

# 请注意，fill_color参数使用了RGBA格式的颜色，其中rgba(255, 0, 0, 0.3)表示红色并带有30%的透明度。fill_opacity参数设置了填充颜色的整体透明度。

# 定义多边形坐标
polygon_coords = [
    [40.727, -74.006],
    [40.727, -73.994],
    [40.712, -73.994],
    [40.712, -74.006]
]

# 添加多边形到地图
folium.Polygon(polygon_coords, color='blue', fill=True, fill_color='blue', fill_opacity=0.5).add_to(m)

# 定义热力图数据
data = [[40.7128, -74.0060], [40.727, -73.994], [40.712, -73.994]]

# 添加热力图到地图
HeatMap(data).add_to(m)

m.save('interactive_map.html')
