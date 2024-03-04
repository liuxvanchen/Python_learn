from collections import Counter


def count_numbers(s):
    lists = Counter(s)
    for item, count in lists.items():
        print("{}出现了{}次".format(item, count))


s = input("enter the list: ")
count_numbers(s)
