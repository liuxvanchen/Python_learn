def insert(s):
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and s[j] > key:
            s[j + 1] = s[j]
            j = j - 1
        s[j + 1] = key
    return s


def get_input_numbers():
    in_str = input("Please input numbers: ")
    numbers = list(map(int, in_str.split()))
    return numbers


s = get_input_numbers()
print(insert(s))
