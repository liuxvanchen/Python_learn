class Stack:
    def __init__(self):
        self.stack = []

    def push(self, valual):
        self.stack.append(valual)

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return (len(self.stack))


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while True:
        print("Enter the operation you want:")
        print("1 - push")
        print("2 - peek")
        print("3 - pop")
        print("4 - size")
        print("5 - quit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            val = input("Enter the value you want to push: ")
            s.push(val)
            print(s.stack)
        elif choice == '2':
            print("the peek of the stack is ", s.peek())
        elif choice == '3':
            print("pop element is ", s.pop())
        elif choice == '4':
            print("the size of the stack is ", s.size())
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
