from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class circle(Shape):#要在命名时定义上是Shape类的多态（继承？
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


class three(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return 3 * self.l


def calculate(shape: Shape):
    area = shape.area()
    print(f"{shape}'s area is {area}")


circles = circle(4)
threes = three(3)

calculate(circles)
calculate(threes)
