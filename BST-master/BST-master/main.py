import functions

BST_msg = """
Which operation you want to perform on BST
1. Insertion
2. Deletion
3. Print in preorder
4. Search
"""
my_bst = functions.BST()
while True:
    user_choice = input(BST_msg)
    match user_choice:
        case '1':
            size = int(input("How many elements you want to insert into BST : "))
            for i in range(size):
                my_bst.insert_node(int(input("Insert an element : ")))
            print(f"{size} elements inserted successfully!")

        case '2':
            ele_to_del = int(input("Enter a value to delete from BST"))
            my_bst.del_node(ele_to_del)

        case '3':
            my_bst.print_inorder()
        case '4':
            my_bst.search_node(int(input("Enter a value to search")))