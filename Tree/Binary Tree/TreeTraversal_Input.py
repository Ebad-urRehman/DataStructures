# Making Node for a tree
class Node():
    def __init__(self, data):
        self.node_data = data
        self.right = None
        self.left = None

# implementing tree
class Tree:

    def InputTree(self):
        data = int(input(f"Enter node : "))
        if data == -1:
            return None
        root = Node(data)
        self.left = self.inputTree()
        self.right = self.inputTree()
        return root

    def take_input_preorder(self, root):
        temp_stack = []
        # printing first ever node
        print("root")
        while True:
            while root.left is not None:
                if root.right is not None:
                    temp_stack.append(root.right)
                # traversing through left of root
                root = root.left
                print("root")
            if root.left is None:
                if root.right is not None:
                    root = root.right
                elif root.right is None:
                    back_trav = temp_stack.pop
                    root = back_trav
                    break
    def print_tree(self, root):
        if root is None:
            return
        if root is not None:
            print(f"{root.node_data}")
        if root.left is not None:
            print(f"L {root.left.node_data} ,")
        if root.right is not None:
            print(f"R {root.right.node_data}")
        print(root.node_data)
        self.print_tree(root.left)
        self.print_tree(root.right)



    def print_postorder_alg1(self, root, temp_stack):
        while root is not None:
            temp_stack.append(root)
            if root.right is not None:
                temp_stack.append(str(root.right))
                print(temp_stack[-1])
                # print(int(temp_stack[-1]))
            root = root.left
            if root is None:
                poped_ele = temp_stack.pop()
                # if +ive elements are poped meaning roots are poped
                if self.is_instance_node(poped_ele):
                    print(poped_ele.node_data)
                    poped_ele = temp_stack.pop()
                else:
                    address_str = poped_ele[2:]
                    mem_adress = int(address_str, 16)
                    root = mem_adress

if __name__ == "__main__":


    my_tree = Tree()
    root = my_tree.inputTree()
    my_tree.take_input_preorder(root)
    