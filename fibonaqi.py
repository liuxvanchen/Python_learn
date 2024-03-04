def fibonacci(n):
    fib_arr = [0, 1]
    while len(fib_arr) < n:
        fib_arr.append(fib_arr[-1] + fib_arr[-2])
    return fib_arr


n = int(input("enter the number: "))
print(fibonacci(n))
