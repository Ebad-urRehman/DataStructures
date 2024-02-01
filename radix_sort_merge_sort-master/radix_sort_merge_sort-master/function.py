# max_len is the maximum length of a string or number in list
def radix_sort(my_list, max_len):
    n = 1
    current_len = 0
    while current_len != max_len:
        current_len += 1
        junk_list = []
        bucket_list = [None] * 10
        for i, elements in enumerate(my_list):
            ele_to_sort = int((my_list[i]/n) % 10)
            print(ele_to_sort)
            if bucket_list[ele_to_sort] is None:
                bucket_list[ele_to_sort] = [my_list[i]]
            else:
                bucket_list[ele_to_sort].append(my_list[i])
            print(f"unit place : {(my_list[i]/n) % 10}")
            print(my_list[i])
        for i, sub_list in enumerate(bucket_list):
            if sub_list is not None:
                print(sub_list)
                junk_list += sub_list
        my_list = junk_list
        n *= 10
        print(my_list)

def merge_sort(my_list):
    # case where list have only one or zero 0 node then list is already sorted
    if len(my_list) <= 1:
        return my_list
    # finding length of list
    mid = find_mid(my_list)
    left_list = my_list[mid:]
    right_list = my_list[:mid]
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    return merge_list(left, right)

def find_mid(listt):
    total_length = len(listt)
    mid = int(total_length // 2)
    return mid

def merge_list(left, right):
    result = []
    i = j = 0

    # Comparing elements from left and right sublists and merging them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements from left and right
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    # list_my = [23, 1, 45, 234, 5, 7, 89]
    # radix_sort(list_my, max_len=3)

    my_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(my_list)
    print("Original List:", my_list)
    print("Sorted List:", sorted_list)