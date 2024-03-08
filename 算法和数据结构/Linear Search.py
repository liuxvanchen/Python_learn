def linear(s, x):
    for i in range(len(s)):
        if s[i] == x:
            print("the element is in the list, the location is {}".format(i))
            return
    print("the element isn't in the list :(")


def get_input_number():
    in_num = input("Enter the numbers separated by spaces: ")
    numbers = list(map(int, in_num.split()))
    return numbers


# 定义要搜索的元素
a = int(input("Enter the number to search for: "))

# 获取用户输入的数字列表
s = get_input_number()

# 执行线性搜索
linear(s, a)

