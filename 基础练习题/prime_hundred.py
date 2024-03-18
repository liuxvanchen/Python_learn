def prime_judge(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def compare_list(s1, s2):
    if s1 == s2:
        return True
    return False


def compare_set(list1, list2):
    return set(list1) == set(list2)


s = []
for j in range(0, 101):
    if prime_judge(j):
        s.append(j)

print(s)

a1 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
if compare_list(a1, s):
    print("you are right")
else:
    print("the list you find not right")
