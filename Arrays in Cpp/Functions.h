#pragma once
class Arr
{
public:
    int get_total_no();
    void get_array(int arr[], int size);
    void display_array(int arr[], int size);
    void mergeArrays(int arr1[], int arr2[], int arr3[], int n1, int n2);
    void assign_arr(int arr_dest[], int arr_source[], int n);
    void insert_arr(int position, int value,int arr[],int n);
    void get_old_el(int arr[], int n, int& old_el);
    void update_el(int arr[], int n, int old_el, int new_el);
    void bubb_sort(int arr[], int n);
    void selection_sort(int arr[], int n);
    void insertion_sort(int arr[], int n);
    void display_arr_reverse(int arr[], int n);
    void del_el(int arr[], int n, int element);
    void del_by_position(int arr[], int n, int position);
    bool check_element(int arr[], int n, int value);
    void search_el(int arr[], int n, int val);
};