import numpy as np
import matplotlib.pyplot as plt

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

# 定义对流-扩散方程的离散形式
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

# 时间离散化
t = np.linspace(0, T, nt)
dx = L / (nx - 1)

# 使用四阶龙格-库塔方法求解
C = runge_kutta_4(advection_diffusion, C0, t, u, D, nx, dx)

# 绘图展示结果
plt.figure(figsize=(10, 6))
for i in range(0, nt, nt // 10):
    plt.plot(x, C[:, i], label=f't={t[i]:.2f}')

plt.rcParams['font.sans-serif'] = ['SimSun']  # 或者 ['Microsoft YaHei']
plt.title('污染物浓度随时间的变化 (龙格-库塔方法)')
plt.xlabel('位置 x')
plt.ylabel('浓度 C')
plt.legend()
plt.grid(True)
plt.show()
