class Person:
    def __call__(self, name):
        print("__call__"+" Hello "+name)

    def hello(self,name):
        print("hello"+name)


class MyClass:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y


obj = MyClass(5)
print(obj)
result = obj(3)  # 这里调用了 obj 实例对象，实际上就是调用了 obj 的 __call__ 方法
print(result)  # 输出 8

person=Person()
person("zhangsan")
person.hello("lisi")