class Node:
    # calling the constructor and assigning data to node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.priority = None


class Priority_Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, data, priority):
        newnode = Node(data)
        newnode.next = None
        newnode.priority = priority
        if self.rear is None and self.front is None:
            self.rear = newnode
            self.front = newnode
        elif priority < self.front.priority:
            newnode.next = self.front
            self.front = newnode
        else:
            current = self.front
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            newnode.next = current.next
            current.next = newnode

    def dequeue(self):
        if self.front is None:
            print("Queue is Already Empty")
        elif self.front == self.rear:
            print("Deleting last node\n List is Empty now")
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            print("Node Deleted")

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

    class Node:
        # calling the constructor and assigning data to node
        def __init__(self, data):
            self.data = data
            self.next = None

# creating empty linked list
class Singly_Linked_List:
    def __init__(self):
        self.head = None

    # linklist from user
    def get_linklist(self, total_nodes, count):
        for n in range(total_nodes):
            data = int(input(f"Please Enter data of node {n + 1}\n"))
            newnode = Node(data)
            if not self.head:
                self.head = newnode
                count[0] += 1
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = newnode
                count[0] += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertion_sort(self, count):
        current = self.head
        if self.head is None:
            print("List is Empty")
        elif current.next is None:
            print("List only have one node")
        else:
            while current.next is not None:
                current = current.next
                print("current updated")
                # starting from self.head and comparing until current in while loop
                current_temp = self.head
                while current_temp is not current:
                    if current.data < current_temp.data:
                        temp = current_temp.data
                        current_temp.data = current.data
                        current.data = temp
                        print(current.data)
                        print(current_temp.data)
                    current_temp = current_temp.next
                    print("current_temp updated")
                # i += 1

    def binary_search(self, count, value):
        beg = 0
        current = self.head
        while current.next is not None:
            current = current.next
        end = count[0] - 1
        mid = int((beg+end)/2)
        mid_data = self.head
        for i in range(int(mid) - 1):
            mid_data = mid_data.next
        while beg <= end and value != mid_data.data:
            if value > mid_data.data:
                beg = mid + 1
            else:
                end = mid - 1
            mid = int((beg+end)/2)
            # finding data on mid position
            mid_data = self.head
            for i in range(int(mid) - 1):
                mid_data = mid_data.next

        if mid_data.data == value:
            position = mid
        else:
            position = None
        return position

if __name__ == "__main__":
    my_queue = Priority_Queue()
    my_queue.enqueue(23, 7)
    my_queue.enqueue(89, 9)
    my_queue.enqueue(900, 3)
    my_queue.display_queue()
