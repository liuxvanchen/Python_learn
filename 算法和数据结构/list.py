class Linknode:
    def __init__(self, x):
        self.data = x
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Linknode(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        print()


def main():
    print("1-append")
    print("2-display")
    print("3-quit")
    linklist = Linkedlist()
    while True:
        s = input("Enter the operation of the link:")

        if s == '1':
            val = input("enter the value you want to join: ")
            linklist.append(val)
        elif s == '2':
            linklist.display()
        elif s == '3':
            break
        else:
            print("the operation invaluable")


if __name__ == '__main__':
    main()
