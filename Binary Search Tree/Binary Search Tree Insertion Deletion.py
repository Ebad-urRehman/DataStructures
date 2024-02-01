# implementing binary search tree

class BST_Node():
    def __init__(self, data):
        self.node_data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    # def insert_node(self):
    #     info = int(input("Enter root Node : "))

    # find algorithm finds and return the location and parent of a new value
    def find(self, value):
        if self.root is None:
            parent = None
            location = None
            return parent, location
        if value == self.root.node_data:
            parent = None
            location = self.root
            return parent, location
        current = self.root
        while current is not None:
            save = current
            if value == current.node_data:
                parent = save
                location = current
                return parent, location

            if value < current.node_data:
                current = current.left
            elif value > current.node_data:
                current = current.right

        parent = save
        location = None
        return parent, location

    def insert_node(self, value):
        parent, location = self.find(value)
        if location is not None:
            print("Node already exists!")

        # creating the node
        new_node = BST_Node(value)
        if parent is None:
            self.root = new_node
            print(self.root.node_data)
        else:
            if value < parent.node_data:
                parent.left = new_node
            else:
                parent.right = new_node

    def del_node(self, value):
        parent, location = self.find(value)
        if location is None:
            print("Element to delete not found")
            return
        # case where node has no child nodes
        if not location.left and not location.right:
            node_to_replace = None
        # cases where node has one child
        elif not location.left and location.right:
            node_to_replace = location.right.node_data
            print("right")
        elif not location.right and location.left:
            node_to_replace = location.left.node_data
            print("left")
        # case where node has two childs
        else:
            # finding inorder successor and replacing it by node to delete
            current = location.right
            while current.left:
                save = current
                current = current.left
            node_to_replace = save.left.node_data
            # the inorder successor may have one node i.e. right node replacing it with right node if it exits other
            # wise it will be replaced by None
            save.left = save.left.right
        # condition for whether it is root node or not
        if location != self.root:
            print(f"{parent.node_data} parent")
            if parent.left == location:
                parent.left.node_data = node_to_replace
                print("left")
            elif parent.right == location:
                parent.right.node_data = node_to_replace
                print("right")
        else:
            self.root.node_data = node_to_replace

        print(f"Node with value {value} deleted successfully!")


    def search_node(self, value):
        parent, location = self.find(value)
        if location is None:
            print("Node not found in BST!")
            return
        if location == self.root:
            print("Element found at root node")
        else:
            print(f"Element is present in BST!")
    def print_inorder(self):
        if self.root is None:
            print("BST is empty.")
            return

        temp_stack = []
        current = self.root

        while current is not None or temp_stack:
            while current is not None:
                temp_stack.append(current)
                current = current.left

            current = temp_stack.pop()
            print(current.node_data, end=", ")
            current = current.right

