def select(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            min = s[i]
            if s[j] < min:
                s[i], s[j] = s[j], s[i]
    return s


def get_input_numbers():
    # 让用户输入数字，用空格隔开
    input_str = input("请输入一系列数字，用空格隔开：")
    # 将输入的字符串按空格分割，并转换成整数列表
    numbers = list(map(int, input_str.split()))
    return numbers


# 获取用户输入的数字列表
numbers = get_input_numbers()
# 对列表进行冒泡排序
select(numbers)
# 打印排序后的列表
print("排序后的数字：")
print(numbers)
