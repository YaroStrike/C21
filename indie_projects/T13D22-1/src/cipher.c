#include <stdio.h>
#include "filehandler.h"
#include "filewriter.h"

void processChoice1() {
    char filename[100];
    scanf("%s", filename);
    file_out(filename);
    int choice2;
    scanf("%d", &choice2);
    switch (choice2) {
        case 2:
            char content[100];
            scanf("%s", content);
            file_input(filename, content);
            break;
        case 1:
            processChoice1();
            break;
        case -1:
            // Add a return statement to exit the function
            return;
        default:
            printf("n/a\n");
            break;
    }
}

int main() {
    int choice;

    while (1) {
        scanf("%d", &choice);
        if (choice == 1) {
            int exitFlag = 0; 
            while (!exitFlag) {
                processChoice1();
                scanf("%d", &choice);
                if (choice == -1) {
                    exitFlag = 1; 
                }
            }
            break;
        } else {
            printf("n/a");
            break;
        }
    }

    return 0;
}
