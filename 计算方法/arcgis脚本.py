import arcpy
import numpy as np

# 设置工作环境
arcpy.env.workspace = "path_to_your_workspace"

# 定义微分方程
def advection_diffusion(t, C, u, D, nx, dx):
    dCdt = np.zeros(nx)
    dCdt[1:-1] = -u * (C[2:] - C[:-2]) / (2 * dx) + D * (C[2:] - 2 * C[1:-1] + C[:-2]) / dx**2
    return dCdt

# 四阶龙格-库塔方法
def runge_kutta_4(f, C0, t, u, D, nx, dx):
    dt = t[1] - t[0]
    C = np.zeros((nx, len(t)))
    C[:, 0] = C0
    for i in range(1, len(t)):
        k1 = f(t[i-1], C[:, i-1], u, D, nx, dx)
        k2 = f(t[i-1] + dt/2, C[:, i-1] + dt/2 * k1, u, D, nx, dx)
        k3 = f(t[i-1] + dt/2, C[:, i-1] + dt/2 * k2, u, D, nx, dx)
        k4 = f(t[i-1] + dt, C[:, i-1] + dt * k3, u, D, nx, dx)
        C[:, i] = C[:, i-1] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    return C

# 定义参数
u = 1.0  # 流体速度
D = 0.1  # 扩散系数
L = 10.0  # 空间范围
T = 5.0  # 时间范围
nx = 100  # 空间步数
nt = 200  # 时间步数

# 定义初始条件
x = np.linspace(0, L, nx)
C0 = np.exp(-10 * (x - 2)**2)
t = np.linspace(0, T, nt)
dx = L / (nx - 1)

# 使用四阶龙格-库塔方法求解
C = runge_kutta_4(advection_diffusion, C0, t, u, D, nx, dx)

# 将结果保存到ArcGIS中
output_table = "pollution_simulation_results"
arcpy.CreateTable_management(arcpy.env.workspace, output_table)
arcpy.AddField_management(output_table, "Time", "DOUBLE")
arcpy.AddField_management(output_table, "Concentration", "DOUBLE")

# 插入模拟结果
cursor = arcpy.da.InsertCursor(output_table, ["Time", "Concentration"])
for i in range(nt):
    for j in range(nx):
        cursor.insertRow([t[i], C[j, i]])

del cursor

print("Simulation completed and results saved to ArcGIS table.")
