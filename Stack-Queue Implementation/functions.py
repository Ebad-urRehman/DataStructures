from array import *


class Stack_arr:
    def __init__(self):
        self.size = int(input("Enter Capacity of Stack as you want"))
        self.stack = array('i', [0] * int(self.size))
        self.top = -1
        self.total = int(self.size)

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def return_top(self):
        return self.top

    def push(self, value):
        if self.top == self.total - 1:
            print("Stack is full\n OVERFLOW")
        else:
            self.top += 1
            self.stack[self.top] = int(value)
            print("Value Pushed Successfully")

    def pop(self):
        if self.top == -1:
            print("Stack is Empty\n UNDERFLOW")
        else:
            value = self.stack[self.top]
            self.stack[self.top] = 0
            self.top -= 1
            print(f"___Last value {value} Popped from the stack___")
            return value

    def display_stack(self):
        if self.top == -1:
            print("Stack is empty")
        for index in range(self.top + 1):
            print(self.stack[index])

    def display_stack_rev(self):
        if self.top == -1:
            print("Stack is Empty")
        start = self.top
        for index in range(start, -1, -1):
            print(self.stack[index])


# Stack list functions
class Stack_Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_List():
    def __init__(self):
        self.head = None
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        newnode = Stack_Node(data)
        if self.is_empty():
            self.top = newnode
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            self.top = newnode


    def pop(self):
        if self.is_empty():
            print("Stack is Already Empty")
        else:
            current = self.head

            while current.next is not self.top:
                current = current.next
                if current is None:
                    self.top = None
                    self.head = None
                    break
            if current:
                del current.next
                self.top = current
                current.next = None

    def display_stack(self):
        if self.head is None:
            print("Stack is Empty")
        current = self.head
        while current is not None:
            print(current.data, end="\n")
            current = current.next
        # print(current.data)


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
            self.front = None
            self.rear = None
            count[0] -= 1
        else:
            self.front += 1
            count[0] -= 1

    def display_queue(self, count):
        print("front ->", end="")
        i = self.front
        try:
            while i != self.rear + 1:
                print(self.queue[i], end="-")
                i += 1
        except Exception:
            print("")
        print("<- rear")



# Queue Linked list functions

class Node():
    # calling the constructor and assigning data to node
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, data):
        newnode = Node(data)
        if self.rear is None and self.front is None:
            self.rear = newnode
            self.front = newnode
        else:
            self.rear.next =newnode
            self.rear = newnode
            newnode.next = None

    def dequeue(self):
        if self.front is None:
            print("Queue is Already Empty")
        elif self.front == self.rear:
            print("Deleting last node\n List is Empty now")
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next

    def display_queue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            current = self.front
            print("front->", end="")
            while current is not None:
                print(current.data, end=", ")
                current = current.next
            print("<-rear")