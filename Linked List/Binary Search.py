class Node:
        # calling the constructor and assigning data to node
        def __init__(self, data):
            self.data = data
            self.next = None


# creating empty linked list
class SinglyLinkedList:
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

    # binary search defination
    def BinarySearch(self, count, value):
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
                print(mid)
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
                position = int(mid)
            else:
                print(mid)
                position = None
            return position
    

if __name__ == "__main__":
    count = [0]
    total_nodes = int(input("How many nodes you want in binary tree : "))
    my_list = SinglyLinkedList()
    my_list.get_linklist(total_nodes, count)
    value = int(input("Enter a value to find through binary search : "))
    position = my_list.BinarySearch(count, value)
    print(f"Value{value} find at position {position}")