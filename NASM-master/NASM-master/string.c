#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
int main()
{
    char a = 'a';
    char b = 'b';
    char c = 'c';
    char space = ' ';
    char chardig = '1';
    // bool check = 'A' == 'A';
    printf("%d \n",'A'=='A');
    printf("a+1= %c \n",a+1);
    printf("c-a= %d \n",c-a);
    printf("total_alpha = %d", 'z'-a+1);
    bool check = isalpha(a);
    printf("%d \n", isalpha(a));
    printf("%d", check);
    if(isalpha(a))
    {
        printf("%c is an alphabet\n", a);
    }
    if(islower(a))
    {
        printf("%c is an lower case alpha\n", a);
    }
    if(isspace(space))
    {
        printf("%c is a space\n", space);
    }
    if(isdigit(chardig))
    {
        printf("%d is chardig",chardig);
    }
    char lowercase = 'a';
    char upper_case = toupper(lowercase);
    printf("%c to upper case is %c\n", lowercase, upper_case);
    // bool var = isalpha(a);
    bool isLetter = isalpha('a');
    if(isLetter)
    {
        printf("%c is alplha\n", 'a');
    }
    char new = 'Z';
    if(isupper(new))
    {
        printf("%c is upper case\n",new);
    }
    char arr[9];
    //  = "hello world\n";
    printf("%s \n", arr);
    for (int i = 0; i < 10; i++)
    {
        scanf("%c", &arr[i]);

    }
    printf("%s \n", arr);
    *arr='c';//first adress
    *(arr+1) = 'a';
    printf("%s \n", arr);
    for (int i = 0; i < 10; i++)
    {
        printf("%c", arr[i]);

    }
    int lenght= strlen(arr);
    printf("%d", lenght);
}