import functions

Pri_Que_Msg = """
Which Operation You want to perform
1. Priority Queue on list
2. Insertion Sort on List
3. Binary Search on List
4. Exit
"""
Q_msg = """
Enter E for enqueue
Enter D for dequeue
Enter q to quit
"""

while True:
    user_choice = input(Pri_Que_Msg)

    match user_choice:
        case '1':
            my_queue = functions.Priority_Queue()
            while True:
                Q_choice = input(Q_msg)
                Q_choice = Q_choice.capitalize()
                match Q_choice:
                    case 'E':
                        data = int(input("Enter the value to enqueue"))
                        priority = int(input("Enter the priority of Node"))
                        my_queue.enqueue(data=data, priority=priority)
                        my_queue.display_queue()

                    case 'D':
                        my_queue.dequeue()
                        print("Deleting Node From Front End....")
                        print("One Node from front deleted")
                        my_queue.display_queue()
                    case 'Q':
                        break

        case '2':
            while True:
                count = [0]
                size = int(input("Enter total number of nodes you want in Link list"))
                my_linked_list = functions.Singly_Linked_List()
                my_linked_list.get_linklist(size, count)
                print("List before sorting is")
                my_linked_list.print_list()
                insertion_sort = input("Enter S to sort the array")
                insertion_sort = insertion_sort.capitalize()
                if insertion_sort == 'S':
                    my_linked_list.insertion_sort(count)
                    print("List after Insertion sort is : ")
                    my_linked_list.print_list()
                exit_ch = input("Enter E to exit any other character to enter another link list")
                exit_ch = exit_ch.capitalize()
                if exit_ch == 'E':
                    break

        case '3':
            while True:
                    count = [0]
                    size = int(input("Enter total number of nodes you want in Link list"))
                    my_linked_list = functions.Singly_Linked_List()
                    my_linked_list.get_linklist(size, count)
                    value = int(input("Enter which value you want to search in link list"))
                    position = my_linked_list.binary_search(count, value)
                    print(f"{value} found at position {position}")
                    exit_ch = input("Enter E to exit any other character to enter another link list")
                    exit_ch = exit_ch.capitalize()
                    if exit_ch == 'E':
                        break

