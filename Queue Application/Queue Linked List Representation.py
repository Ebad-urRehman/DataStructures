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

if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(23)
    my_queue.enqueue(89)
    my_queue.enqueue(900)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.display_queue()