import numpy as np

#找最大公约数
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

arr = np.array([20, 8, 32, 36, 16])
x1 = np.gcd.reduce(arr)
print(x1)