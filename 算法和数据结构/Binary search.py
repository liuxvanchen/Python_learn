def binary(s, x, start, end):
    if start <= end:
        middle = (start + end) // 2
        if x == s[middle]:
            print("You have found the location: {}".format(middle))
        elif x > s[middle]:
            binary(s, x, middle + 1, end)
        else:
            binary(s, x, start, middle - 1)
    else:
        print("The element isn't in the list :(")


def get_input_numbers():
    in_str = input("Please input numbers separated by spaces: ")
    numbers = list(map(int, in_str.split()))
    return numbers


a = int(input("Enter the number to search for: "))
s = get_input_numbers()
s.sort()
binary(s, a, 0, len(s) - 1)

