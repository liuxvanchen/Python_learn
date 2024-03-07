from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):  # 入队
        self.queue.append(value)

    def dequeue(self):  # 出队
        if not self.is_empty():  # 判断是否为空
            return self.queue.popleft()  # 左端出，在deque库里，pop默认右端出
        else:
            return "Queue is empty"

    def peek(self):  # 求队列头元素，所以是queue【0】
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


def main():
    q = Queue()
    q.enqueue(6)
    q.enqueue(5)

    while True:
        print("Enter the operation you want:")
        print("1 - enqueue")
        print("2 - peek")
        print("3 - dequeue")
        print("4 - size")
        print("5 - quit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            val = input("Enter the value you want to push: ")
            q.enqueue(val)
            print(q.queue)
        elif choice == '2':
            print("the peek of the stack is ", q.peek())
        elif choice == '3':
            print("pop element is ", q.dequeue())
        elif choice == '4':
            print("the size of the stack is ", q.size())
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
