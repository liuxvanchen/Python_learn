from Greatest_Common import greatest_common


def little_common(a, b):
    greatest = greatest_common(a, b)
    little = (a * b) / greatest
    return little


# 获取输入字符串
input_str = input("请输入两个整数，用逗号分隔：")
# 使用split()方法根据逗号分隔输入字符串
params = input_str.split(',')

# 去除可能的前后空格，并将结果存储在param1和param2中
param1, param2 = params[0].strip(), params[1].strip()

# 将字符串转换为整数
param1, param2 = int(param1), int(param2)

# 调用函数并打印结果
print(little_common(param1, param2))
