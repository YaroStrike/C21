#include <stdio.h>
int main()
{
    //массив int, в одной строке.
    int arr[] = {0, 2, 3, 4, 5, 6};
    arr[0] = 1; //замена значения элемента.
    printf("%d\n", arr);

    //массив float, с отдельной инициализацией.
    float numbers[3];
    numbers[0] = 1.11;
    numbers[1] = 2.22;
    numbers[2] = 3.33;
    numbers[3] = 4.44;
    printf("%d\n", numbers);
}