def odd(n):
    if n == 0:
        return True
    else:
        if n % 2 == 0:
            return True
        else:
            return False


n = int(input("enter the number you want to judge: "))
if odd(n):
    print("the number {} you inter isn't odd".format(n))
else:
    print("the number you enter is odd")
