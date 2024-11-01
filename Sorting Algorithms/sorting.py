import numpy as np

def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                min = j
        list[min], list[i] = list[i], list[min]
    print(list)
            
        
def merge_sort(arr, start, end):
    if start < end:
        mid = int((start + end)/2)
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
        

def merge(arr, start, mid, end):
    left_sublist = arr[start:mid+1]
    right_sublist = arr[mid+1:end+1]
    
    i = 0
    j = 0
    k = start
    
    while i<len(left_sublist) and j<len(right_sublist):
        if left_sublist[i] <= right_sublist[j]:
            arr[k] = left_sublist[i]
            i+=1
        else:
            arr[k] = right_sublist[j]
            j+=1
        k+=1
    
    # copy remaining element to the array
    while i<len(left_sublist):
        arr[k] = left_sublist[i]
        i+=1
        k+=1
        
    while j<len(right_sublist):
        arr[k] = right_sublist[j]
        j+=1
        k+=1
    
            
    
if __name__ == '__main__':
    arr = [6, 4, 5 ,2, 1]
    print(arr)
    merge_sort(arr, 0, 4)
    print('sorted array is arr', arr)