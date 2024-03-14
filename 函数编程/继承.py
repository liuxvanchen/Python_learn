class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is make sound")


class Dog(Animals):
    def speak(self):
        print(f"{self.name} is bark")


my_dog = Dog("bubu")

my_dog.speak()
