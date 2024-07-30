#include <stdio.h>
int main() {
    char string[255];
    printf("Введите строку -> ");
    //scanf("%s", string);
    // чтобы вывести настоящую строку с пробелами, нужно выполнить функцию fgets():
    fgets(string, sizeof(string), stdin);
    printf("Вы ввели: %s\n", string);
    return 0;
}
