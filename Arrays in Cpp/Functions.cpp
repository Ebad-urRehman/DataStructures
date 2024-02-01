#include <iostream>
#include "Functions.h"
using namespace std;


int Arr::get_total_no()
{
    int size;
    cout << "How many elements you want in array : ";

    while (true)
    {
        cin >> size;
        if (cin.fail())
        {
            cin.clear();  // Clear the fail state
            cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // Clear the input buffer
            cout << "Invalid input. Please enter a valid integer." << endl;
            cout << "\a";
        }
        else
        {
            break;
        }
    }
    return size;
}

void Arr::get_array(int arr[], int size)
{
    cout << "Start entering elements in array : \n";
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
}

void Arr::display_array(int arr[], int size)
{
    cout << "\n\n\nThe Elements in your array are: \n";
    for (int i = 0; i < size; i++)
    {
        cout << arr[i]<<",";
    }
    cout << endl;
}
void Arr::mergeArrays(int arr1[], int arr2[], int arr3[], int n1, int n2)
{
    int i, j;
    for (i = 0; i < n1; i++)
    {
        arr3[i] = arr1[i];
    }
    for (j = 0; j < n2; j++)
    {
        arr3[i + j] = arr2[j];
    }
}

void Arr::assign_arr(int arr_dest[], int arr_source[], int n)
{
    for (int i = 0; i < n; i++)
    {
        arr_dest[i] = arr_source[i];
    }
}

void Arr::insert_arr(int position, int value, int arr[], int n)
{
    for (int i = n; i >= position; i--)
    {
        //for first time i is position means index - 1
        arr[i] = arr[i - 1];
    }
    arr[position - 1] = value;
}


void Arr::get_old_el(int arr[], int n, int& old_el)
{
    int test = 0;
    while (true)
    {
        cout << "Which element you want to update : ";
        cin >> old_el;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == old_el)
            {
                test = old_el;
                break;
            }
        }
        if (old_el == test)
        {
            break;
        }
        else
        {
            cout << "Element not found :( Try Again \n";
        }
    }
}

void Arr::update_el(int arr[], int n, int old_el, int new_el)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == old_el)
        {
            arr[i] = new_el;

        }
    }
}

void Arr::bubb_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }

    }
}

void Arr::selection_sort(int arr[], int n)
{
    int temp;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}



void Arr::insertion_sort(int arr[], int n)
{
    int key, j;
    for (j = 0; j < n; j++)
    {
        key = arr[j];
        int i = j - 1;
        while (i >= 0 && arr[i] > key)
        {
            arr[i + 1] = arr[i];
            i--;
        }
        arr[i + 1] = key;

    }
}

void Arr::display_arr_reverse(int arr[], int n)
{
    for(int i = n - 1; i >= 0; i--)
    {
        cout << arr[i] << ",";
    }
    cout<<endl;
}

void Arr::del_el(int arr[], int n, int element)
{
    if (n == 0)
    {
        cout << "Array is empty delete this array in main menu and enter a new array";
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == element)
            {
                for (int j = i; j < n - 1; j++)
                {
                    arr[j] = arr[j + 1];
                }
            }
        }
    }
}

void Arr::del_by_position(int arr[], int n, int position)
{
    if (n == 0)
    {
        cout << "Array is empty delete this array in main menu and enter a new array";
    }
    else
    {
        for (int j = position-1; j < n - 1; j++)
        {
            arr[j] = arr[j + 1];
        }
    }
}

bool Arr::check_element(int arr[], int n, int value)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == value)
        {
            return true;
        }
    }
        return false;
}

void Arr::search_el(int arr[], int n, int val)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == val)
        {
            cout << "Element found at position " << i + 1<<endl;
            return;
        }
    }
    cout << "Element not present in array\n";
}
