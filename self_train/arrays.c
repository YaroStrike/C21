#include <stdio.h>
int main()
{
    //массив int, в одной строке.
    int arr[] = {0, 2, 3, 4, 5, 6};
    arr[0] = 1; //замена значения элемента.
    int n = sizeof(arr)/sizeof(arr[0]); //деление общего размера массива на размер одного элемента.
    for (int i = 0; i < n; i++)
    {
        printf("%d", arr[i]);
        if (i < n - 1)
        {
            printf(", ");
        }
    }
    //массив float, с отдельной инициализацией.
    float numbers[3];
    numbers[0] = 1.11;
    numbers[1] = 2.22;
    numbers[2] = 3.33;
    numbers[3] = 4.44;
    printf("%d\n", numbers);
}