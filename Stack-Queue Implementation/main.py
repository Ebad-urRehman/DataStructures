import functions
from functions import *
sa_count = [0]
main_menu_msg = """
Which operation you want to perform
1. Stack Array
2. Stack Linked List
3. Queue Array
4. Queue Linked List
"""
stack_arr_msg = """
Which operation you want to perform
1. Push
2. Pop
3. Exit
"""
stack_list_msg = """
1. Push
2. Pop
3. Exit
"""
queue_msg = """
1. Enqueue
2. Dequeue
3. Exit
"""

while True:
    choice = input(main_menu_msg)
    match choice:
        case '1':
            my_arr_stack = functions.Stack_arr()
            while True:
                arr_stack_choice = input(stack_arr_msg)
                match arr_stack_choice:
                    case '1':
                        value = int(input("Enter a value to Push : "))
                        my_arr_stack.push(value)
                        my_arr_stack.display_stack()
                    case '2':
                        del_val = my_arr_stack.pop()
                        my_arr_stack.display_stack()
                    case '3':
                        break

        case '2':
            my_list_stack = functions.Stack_List()
            while True:
                arr_stack_choice = input(stack_list_msg)
                match arr_stack_choice:
                    case '1':
                        value = int(input("Enter a value to Push : "))
                        my_list_stack.push(value)
                        my_list_stack.display_stack()
                    case '2':
                        del_val = my_list_stack.pop()
                        my_list_stack.display_stack()
                    case '3':
                        break
        case '3':
            my_arr_queue = functions.Queue_arr()
            count = [0]
            while True:
                arr_queue_choice = input(queue_msg)
                match arr_queue_choice:
                    case '1':
                        value = int(input("Enter a value to enqueue"))
                        try:
                            my_arr_queue.enqueue(value, count)
                        except IndexError:
                            print("Overflow")
                        my_arr_queue.display_queue(count)
                    case '2':
                        my_arr_queue.dequeue(count)
                        print("Element dequeued")
                        my_arr_queue.display_queue(count)
                    case '3':
                        break
        case '4':
            my_list_queue = functions.Queue()
            while True:
                list_queue_choice = input(queue_msg)
                match list_queue_choice:
                    case '1':
                        value = int(input("Enter a value to enqueue"))
                        my_list_queue.enqueue(value)
                        my_list_queue.display_queue()
                    case '2':
                        my_list_queue.dequeue()
                        print("Element from front dequeued")
                        my_list_queue.display_queue()
                    case '3':
                        break

        case '5':
            print("Program Exited")
            break