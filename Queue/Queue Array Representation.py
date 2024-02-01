from array import *


class Queue_arr:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = int(input("Enter Capacity of Queue as you want : "))
        self.queue = array('i', [0] * int(self.size))

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def is_full(self, count):
        if self.front == self.rear + 1 or self.front == 0 and self.rear == self.size:
            return True
        else:
            return False

    def enqueue(self, data, count):
        if self.rear is None:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            count[0] += 1
        elif self.is_full(count):
            print("Overflow")
            return
        else:
            self.rear += 1
            self.queue[self.rear] = data
            count[0] += 1

    def dequeue(self, count):
        if self.is_empty():
            print("Underflow")
            return
        elif self.front == self.rear and self.front is not None:
            self.queue[self.front] = 0
            self.front = None
            self.rear = None
            count[0] -= 1
        else:
            self.front -= 1
            count[0] -= 1

    def display_queue(self, count):
        print("front ->", end="")
        for i in range(int(count[0])):
            print(self.queue[i], end="-")
        print("<- rear")


if __name__ == "__main__":
    count = [0]
    my_queue = Queue_arr()
    my_queue.enqueue(123, count)
    my_queue.enqueue(789, count)
    my_queue.enqueue(190, count)
    my_queue.enqueue(190, count)
    my_queue.enqueue(190, count)
    my_queue.enqueue(190, count)

    my_queue.display_queue(count)
