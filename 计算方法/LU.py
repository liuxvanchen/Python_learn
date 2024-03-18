import numpy as np


def lu_decomposition_with_gaussian_elimination(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=float)  # 初始化L为单位矩阵

    for i in range(n):
        # 对于每一列进行处理
        for j in range(i + 1, n):
            # 计算L中的系数
            L[j, i] = U[j, i] / U[i, i]
            # 对于U进行行减法操作，实现高斯消去
            for k in range(i, n):
                U[j, k] -= L[j, i] * U[i, k]

    return L, U


A = np.array([[2, 1, 4], [4, 4, 1], [6, 5, 12]], dtype=float)
L, U = lu_decomposition_with_gaussian_elimination(A)
print("L:")
print(L)
print("U:")
print(U)


