#include <iostream>
#include "Functions.h"
#include <conio.h>
using namespace std;
int main()
{
	while (true)
	{
		Arr array;
		int n = array.get_total_no();
		int* arr = new int[n];
		array.get_array(arr, n);
		array.display_array(arr, n);

		//array is created now
		int arr_status = true;

		//Declaring variables needed for merge operation
		int n2, n3;
		int* arr2 = nullptr;
		int* arr_new = nullptr;

		//Declaring variables needed for insertion operation
		int* arr_temp = nullptr;

		//turn variable for formatting output
		int turn = 1;
		while (true)
		{
			char choice;
			if (turn == 1)
			{
				cout << "---------------------------------Main Menu-----------------------------------------";
				cout << "\n\n\n\n---Which operation you want to perform on your array : ---\n";
				cout << "M for Merge(Add new array to existing array)\n";
				cout << "-> I for Insert(Insert new element at desired position)\n";
				cout << "E for Edit(Edit Old element from your desired position)\n";
				cout << "U for Update(Add a new element at last)\n";
				cout << "-> S for Sort (Ascending/Decending)\n";
				cout << "-> Q for search an element in array\n";
				cout << "-> D for deleting an element\n";
				cout << "X for deleting the whole array\n";
			}
			if (turn != 1)
			{
				cout << "\n\n\n.....................Press Backspace to open help menu..............................\n";
			}
			cout << ".....................Press Esc to Exit the program..............................\n\n\n";
			choice = _getch();
			turn++;
			switch (choice)
			{
			case 'M':
				cout << "-----------------------Merging arrays---------------------------\n\n";
				//Entering 2nd array
				cout << "Enter total number of element in second array : ";
				cin >> n2;
				cout << "Enter another array to merge with old array list: \n";
				arr2 = new int[n2];
				array.get_array(arr2, n2);

				//declaring 3rd array to merge both arrays into it
				n3 = n + n2;
				arr_new = new int[n3];
				cout << "Merging Arrays .... \n\n";
				array.mergeArrays(arr, arr2, arr_new, n, n2);

				//making arr_new name arr again by making a new array named arr
				//this is helps if user want to perform any other operation on array
				n = n3;
				arr = new int[n];
				array.assign_arr(arr, arr_new, n);

				//Display user new array
				cout << "Your array list is now : \n";
				array.display_array(arr, n);

				//deleting old arrays
				delete[] arr2;
				delete[] arr_new;
				break;

			case 'I':
				char insertion_choice;
				while (true)
				{
					cout << "\n\n\n--------------------Insertion Menu---------------------";
					cout << "\n\nWhere do you want to insert your element\n\n\n";
					cout << "F. At first Press F\n";
					cout << "L. At Last Press L\n";
					cout << "N. At nth postion Press N\n";
					cout << "......Press Backspace to return to main menu...........\n\n\n\n";
					insertion_choice = _getch();
					switch (insertion_choice)
					{
						int value;
					case 'N':
						int position;
						while (true)
						{
							cout << "Enter position : \n";
							cin >> position;
							if (position <= 0 || position > n + 1)
							{
								cout << "\n\nPlease Enter position in range 1-" << n + 1 << endl;
								cout << "\a";
							}
							else
							{
								break;
							}
						}
						cout << "Value to insert at that position : \n";
						cin >> value;

						//creating temp_arr of capacity +1 and copying all arr in temp array
						n++;
						arr_temp = new int[n];
						array.assign_arr(arr_temp, arr, n);

						//inserting new element to temp array
						array.insert_arr(position, value, arr_temp, n);

						//deleting previous array
						delete[] arr;

						//creating new array with same name
						arr = new int[n];

						//copying temp array back to arr
						array.assign_arr(arr, arr_temp, n);

						//deleting temp array
						delete[] arr_temp;
						array.display_array(arr, n);
						break;

					case 'F':
						cout << "Value to insert at First position : \n";
						cin >> value;

						//creating temp_arr of capacity +1 and copying all arr in temp array
						n++;
						arr_temp = new int[n];
						array.assign_arr(arr_temp, arr, n);

						//inserting new element to temp array at first
						array.insert_arr(1, value, arr_temp, n);

						//deleting previous array
						delete[] arr;

						//creating new array with same name
						arr = new int[n];

						//copying temp array back to arr
						array.assign_arr(arr, arr_temp, n);

						//deleting temp array
						delete[] arr_temp;
						array.display_array(arr, n);
						break;

					case 'L':
						cout << "Value to insert at Last position : \n";
						cin >> value;

						//creating temp_arr of capacity +1 and copying all arr in temp array
						n++;
						arr_temp = new int[n];
						array.assign_arr(arr_temp, arr, n);

						//inserting new element to temp array at last
						array.insert_arr(n, value, arr_temp, n);

						//deleting previous array
						delete[] arr;

						//creating new array with same name
						arr = new int[n];

						//copying temp array back to arr
						array.assign_arr(arr, arr_temp, n);

						//deleting temp array
						delete[] arr_temp;
						array.display_array(arr, n);
						break;
					default:
						cout << "Please Enter Correct Values\n\n";
						cout << "\a";
					}
					if (int(insertion_choice) == 8)
					{
						break;
					}
				}
				break;
			case 'E':
				cout << "\n\n\n---------------Edit An Element----------------\n\n";
				int old_el;
				int new_el;
				array.get_old_el(arr, n, old_el);
				cout << "Enter an element to replace " << old_el << " with : ";
				cin >> new_el;
				cout << "Replacing element " << old_el << " with " << new_el << " .....\n";
				array.update_el(arr, n, old_el, new_el);
				cout << "Your array is now : ";
				array.display_array(arr, n);
				break;
			case 'S':
				cout << "------------------------Sorting-------------------------";
				char sort_choice;
				while (true)
				{
					cout << "\n\n\n\nWhich type of Sort you want to perform : \n";
					cout << "Press\n";
					cout << "B for Bubble sort(Ascending)\n";
					cout << "I for Insertion sort(Ascending)\n";
					cout << "S for selection sort(Ascending)\n";
					cout << "b for Bubble sort(Descending)\n";
					cout << "i for Insertion sort(Descending)\n";
					cout << "s for selection sort(Descending)\n";
					cout << "Press Backspace to return to main menu\n";
					sort_choice = _getch();
					switch (sort_choice)
					{
					case 'B':
						cout << "\n\n\nSorting Ascending by Bubble sort method\n";
						array.bubb_sort(arr, n);
						cout << "\n\n-------Bubble sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_array(arr, n);
						break;
					case 'S':
						cout << "\n\n\nSorting Ascending by Selection sort method.................\n";
						array.selection_sort(arr, n);
						cout << "\n\n-------Selection sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_array(arr, n);
						break;
					case 'I':
						cout << "\n\n\nSorting Ascending by Insertion sort method....................\n";
						array.insertion_sort(arr, n);
						cout << "\n\n-------Insertion sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_array(arr, n);
						break;
					case 'b':
						cout << "\n\n\nSorting Descending by Bubble sort method\n";
						array.bubb_sort(arr, n);
						cout << "\n\n-------Bubble sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_arr_reverse(arr, n);
						break;
					case 's':
						cout << "\n\n\nSorting Descending by Selection sort method.................\n";
						array.selection_sort(arr, n);
						cout << "\n\n-------Selection sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_arr_reverse(arr, n);
						break;
					case 'i':
						cout << "\n\n\nSorting Descending by Insertion sort method....................\n";
						array.insertion_sort(arr, n);
						cout << "\n\n-------Insertion sorting completed--------\n";
						cout << "----Your array is now------\n";
						array.display_arr_reverse(arr, n);
						break;
					default:
						if (int(sort_choice) != 8)
						{
							cout << "\n\n\nPlease Enter correct value..";
							cout << "\a";
							break;
						}


					}
					if (int(sort_choice) == 8)
					{
						break;
					}
				}
				break;
			case 'D':
				cout << "\n\n\n-------------------Deletion Menu------------------";
				char del_choice;
				int val_to_del;
				int position;
				while (true)
				{
					cout << "\n\n------------How you want to delete the element------------\n";
					cout << "E. By element value(Enter element value to delete that element from the array) Press E\n";
					cout << "P. By position(Enter position of element in array to delete that element) Press P\n";
					cout << "............Press Backspace to return to main menu..........\n\n";
					del_choice = _getch();
					switch (del_choice)
					{
					case 'E':
						cout << "\n\nEnter the value to delete : \n";
						bool check_value;
						while (true)
						{
							while (true)
							{
								cin >> val_to_del;
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
							//check if value entered is present in array
							check_value = array.check_element(arr, n, val_to_del);
							if (check_value == true)
							{
								cout << "Deleting value...................\n";

								array.del_el(arr, n, val_to_del);

								// reducing size
								n--;
								// creating a temp array with capicity of n-1
								arr_temp = new int[n];

								//assigning actual array elements to temp array
								array.assign_arr(arr_temp, arr, n);

								//deleting old array
								delete[] arr;

								//creating a new array with old name
								arr = new int[n];

								//assigning temp array back to new array with same name as previous one
								array.assign_arr(arr, arr_temp, n);

								//deleting temp array
								delete[] arr_temp;
								cout << "\n---Element Deleted---\n";
								array.display_array(arr, n);
								break;
							}
							else if (check_value == false)
							{
								cout << "\a";
								cout << "Enter a value present in array\n";
								array.display_array(arr, n);
							}
						}
						break;
					case 'P':
						int pos_choice;
						cout << "\n\n\nFrom where you want to delete the element?\n\n\n";
						cout << "1. From first Press F\n";
						cout << "2. From Last Press L\n";
						cout << "3. At nth postion Press N\n";
						cout << "......Press Backspace to return to main menu...........\n\n";
						pos_choice = getch();
						switch (pos_choice)
						{
						case 'F':
							array.del_by_position(arr, n, 1);

							// reducing size
							n--;

							// creating a temp array with capicity of n-1
							arr_temp = new int[n];

							//assigning actual array elements to temp array
							array.assign_arr(arr_temp, arr, n);

							//deleting old array
							delete[] arr;

							//creating a new array with old name
							arr = new int[n];

							//assigning temp array back to new array with same name as previous one
							array.assign_arr(arr, arr_temp, n);

							//deleting temp array
							delete[] arr_temp;
							cout << "---First element deleted---\n";
							cout << "-----Your array is now-----\n";
							array.display_array(arr, n);
							break;
						case 'L':
							array.del_by_position(arr, n, n);

							// reducing size
							n--;

							// creating a temp array with capicity of n-1
							arr_temp = new int[n];

							//assigning actual array elements to temp array
							array.assign_arr(arr_temp, arr, n);

							//deleting old array
							delete[] arr;

							//creating a new array with old name
							arr = new int[n];

							//assigning temp array back to new array with same name as previous one
							array.assign_arr(arr, arr_temp, n);

							//deleting temp array
							delete[] arr_temp;
							cout << "---Last element deleted---\n";
							cout << "-----Your array is now-----\n";
							array.display_array(arr, n);
							break;
						case 'N':
							cout << "Enter the Position to delete element at that position\n";
							while (true)
							{
								cout << "Enter position : \n";
								while (true)
								{
									cin >> position;
									if (cin.fail())
									{
										cout << "\a";
										cin.clear();  // Clear the fail state
										cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');  // Clear the input buffer
										cout << "Invalid input. Please enter a valid integer." << endl;
									}
									else
									{
										break;
									}
								}
								if (position <= 0 || position > n)
								{
									cout << "\a";
									cout << "\n\nPlease Enter position in range 1-" << n << endl;
								}
								else
								{
									break;
								}
							}
							array.del_by_position(arr, n, position);

							// reducing size
							n--;

							// creating a temp array with capicity of n-1
							arr_temp = new int[n];

							//assigning actual array elements to temp array
							array.assign_arr(arr_temp, arr, n);

							//deleting old array
							delete[] arr;

							//creating a new array with old name
							arr = new int[n];

							//assigning temp array back to new array with same name as previous one
							array.assign_arr(arr, arr_temp, n);

							//deleting temp array
							delete[] arr_temp;

							cout << position << "th Element deleted\n";
							cout << "-----Your Array is now-----\n";
							array.display_array(arr, n);
							break;
						default:
							cout << "\nPlease Enter correct value\n";
							cout << "\a";
							break;
						}
						break;
					default:
						cout << "Enter correct value";
						cout << "\a";
						break;
					}
					if (int(del_choice) == 8)
					{
						break;
					}
				}
				break;
			case 'U':
				cout << "\n\n\n----------------Updation Menu------------------\n\n";
				int up_value;
				char up_choice;
				cout << "Value to Update at last of array : \n";
				cin >> up_value;

				//creating temp_arr of capacity +1 and copying all arr in temp array
				n++;
				arr_temp = new int[n];
				array.assign_arr(arr_temp, arr, n);

				//inserting new element to temp array at last
				array.insert_arr(n, up_value, arr_temp, n);

				//deleting previous array
				delete[] arr;

				//creating new array with same name
				arr = new int[n];

				//copying temp array back to arr
				array.assign_arr(arr, arr_temp, n);

				//deleting temp array
				delete[] arr_temp;
				cout << "Value " << up_value << " updated\n";
				array.display_array(arr, n);
				break;
			case 'X':
				cout << "-------------Array deleted-------------\n";
				cout << "Enter a new array to perform operations\n";
				delete arr;
				arr_status = false;
				cout << "\a";
				break;
			case 'Q':
				cout << "\n\n\n------------------Search Menu-----------------------\n\n";
				int search_val;
				cout << "Enter an element to search in array\n";
				cin >> search_val;
				cout << "......Searching element " << search_val << "..........\n";
				array.search_el(arr, n, search_val);
				break;
			default:
				if (int(choice != 8) && int(choice != 27))
				{
					cout << "Please Enter Correct Values\n\n";
					cout << "\a";
					break;
				}
			}
			if (int(choice) == 27)
			{
				break;
			}
			if (int(choice) == 8)
			{
				turn = 1;
			}
			if (arr_status == false)
			{
				break;
			}
		}
		//into the main while true loop
	}
}
