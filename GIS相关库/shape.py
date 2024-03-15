from shapely.geometry import Point, LineString, Polygon

# 创建一个点
point = Point(0, 0)

# 创建一个线
line = LineString([(0, 0), (1, 1), (1, 0)])

# 创建一个多边形
polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])

# 获取点的坐标
print(point.coords)

# 获取线的坐标序列
print(list(line.coords))

# 获取多边形的面积
print(polygon.area)

# 获取多边形的边界
print(polygon.boundary)

# 创建另一个多边形
other_polygon = Polygon([(0.5, 0.5), (1.5, 0.5), (1.5, 1.5), (0.5, 1.5)])

# 计算两个多边形的交集
intersection = polygon.intersection(other_polygon)
print(intersection)

# 计算两个多边形的并集
union = polygon.union(other_polygon)
print(union)

# 计算两个多边形的差集（第一个多边形减去与第二个多边形重叠的部分）
difference = polygon.difference(other_polygon)
print(difference)

# 计算两个多边形的对称差集（只包含在一个多边形中但不在另一个中的部分）
symmetric_difference = polygon.symmetric_difference(other_polygon)
print(symmetric_difference)

# 为点创建一个缓冲区（例如，半径为 0.5 的圆）
buffer = point.buffer(0.5)
print(buffer)

# 计算两个点之间的距离
distance = point.distance(Point(1, 1))
print(distance)

# 检查两个多边形是否相交
intersects = polygon.intersects(other_polygon)
print(intersects)

# 检查一个多边形是否包含另一个多边形
contains = polygon.contains(other_polygon)
print(contains)