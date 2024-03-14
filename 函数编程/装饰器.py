import time  # 导入Python的time模块，用于处理时间相关的操作，比如获取当前时间。


def timer_decorator(func):  # 定义一个名为timer_decorator的函数，它接受一个参数func，这个func通常是我们想要装饰的函数。
    def wrapper(*args, **kwargs):  # 在timer_decorator函数内部，定义了一个名为wrapper的函数，它接受任意数量的位置参数和关键字参数。
        start_time = time.time()  # 调用time模块的time函数，获取当前的时间（以秒为单位的浮点数），并赋值给start_time变量，用于记录函数开始执行的时间。
        result = func(*args, **kwargs)  # 调用传入的func函数，并将wrapper函数接收到的所有参数传递给它。同时，将func的返回值存储在result变量中。
        end_time = time.time()  # 函数执行完毕后，再次调用time模块的time函数，获取当前的时间，并赋值给end_time变量，用于记录函数结束执行的时间。
        print(f"函数 {func.__name__} 执行了 {end_time - start_time:.6f} 秒")  # 打印一条消息，显示函数名和执行时间。使用格式化字符串来保留六位小数。
        return result  # 返回func函数的执行结果，确保wrapper函数的行为与原始函数一致。

    return wrapper  # timer_decorator函数返回wrapper函数对象，这样当装饰器应用到一个函数上时，实际上是返回了这个wrapper函数。


@timer_decorator  # 这是一个装饰器语法糖，它实际上是将下面的my_function函数作为参数传递给timer_decorator函数，
# 并用timer_decorator返回的wrapper函数替换my_function。
def my_function():  # 定义一个名为my_function的函数。
    time.sleep(1)  # 调用time模块的sleep函数，使程序暂停执行1秒，模拟一个耗时操作。
    print("函数执行完毕")  # 打印一条消息，表示函数执行完毕。


# 调用装饰后的函数
my_function()  # 实际上调用的是wrapper函数，而不是原始的my_function。wrapper函数会记录时间，调用my_function，并打印执行时间。