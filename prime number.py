def prime_judge(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("enter the number: "))
if prime_judge(n):
    print("the number is prime number")
else:
    print("sorry the number {} isn't prime number".format(n))
