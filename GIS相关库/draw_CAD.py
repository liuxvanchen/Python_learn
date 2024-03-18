import ezdxf
import matplotlib.pyplot as plt

# 加载DXF文件
doc = ezdxf.readfile("D:\学科资料\地信原理与应用\实验1\实验1\实验1数据\CAD数据/a11.DXF")
modelspace = doc.modelspace()

# 提取线条数据
lines = [e for e in modelspace if e.dxftype() == 'LINE']

# 创建一个新的matplotlib图形
fig, ax = plt.subplots()

# 遍历线条并绘制
for line in lines:
    start = line.dxf.start
    end = line.dxf.end
    ax.plot([start[0], end[0]], [start[1], end[1]], 'b-')

# 设置坐标轴限制以匹配CAD文件范围（如果需要）
# ax.set_xlim(...)
# ax.set_ylim(...)

# 显示图形
plt.show()