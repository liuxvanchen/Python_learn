# list 列表的方法reverse反转整个列表
# def back_judge(s):
#     s_list = list(s)
#     s_back_list = s_list.copy()  # 复制列表
#     s_back_list.reverse()  # 反转复制后的列表
#     if s_list == s_back_list:
#         print("the str is back_read")
#     else:
#         print("the str isn't back_read")
#
#
# s = input("enter the str you want to judge: ")
# back_judge(s)

# 正确的判断回文程序，palindromic

def is_palindromic(s):
    # 全部改成小写并且去除非字符和空格
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


s = input("enter the str you want to judge:")
if is_palindromic(s):
    print("the number is palindromic")
