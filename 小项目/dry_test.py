
def dry_test(s):
    consecutive_negative = False
    for i in range(len(s) - 1):  # 遍历到倒数第二个元素
        if s[i] < 0 and s[i + 1] < 0:  # 检查当前元素和下一个元素是否都是负数
            consecutive_negative = True
            break  # 如果找到，直接跳出循环
    return consecutive_negative


def get_input_numbers():
    # 让用户输入数字，用空格隔开
    input_str = input("请输入一系列数字，用空格隔开：")
    # 将输入的字符串按空格分割，并转换成整数列表
    numbers = list(map(int, input_str.split()))
    return numbers


# 获取用户输入的数字列表
numbers = get_input_numbers()
if dry_test(numbers):
    # 打印排序后的列表
    print("Yes")
