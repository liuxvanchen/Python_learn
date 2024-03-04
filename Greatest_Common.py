def greatest_common(a, b):
    # 如果 a 小于 b，交换它们的值
    if a < b:
        a, b = b, a

        # 当 b 不为 0 时，持续循环
    while b != 0:
        # 计算 a 除以 b 的余数
        remainder = a % b
        # 将 b 的值赋给 a
        a = b
        # 将余数的值赋给 b
        b = remainder

        # 当循环结束时，a 就是最大公约数
    return a


# 获取输入字符串
input_str = input("请输入两个整数，用逗号分隔：")
# 使用split()方法根据逗号分隔输入字符串
params = input_str.split(',')

# 去除可能的前后空格，并将结果存储在param1和param2中
param1, param2 = params[0].strip(), params[1].strip()

# 将字符串转换为整数
param1, param2 = int(param1), int(param2)

# 调用函数并打印结果
print(greatest_common(param1, param2))
