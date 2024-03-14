class Phone:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.charge = 100

    def make_call(self, number):
        print(f"use {self.brand} call {number}")

    def send_number(self, name, massage):
        print(f"use {self.brand} to {name} send {massage}")

    def check_battery(self):
        print(f"{self.brand}'s charge is {self.charge}")


my_phone = Phone('white', 'iPhone')
my_phone.make_call('123456789')
my_phone.send_number('lucy', 'hello')
my_phone.check_battery()

my_phone.charge = 78
my_phone.check_battery()
