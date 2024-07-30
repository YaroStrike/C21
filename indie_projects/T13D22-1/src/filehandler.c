#include "filehandler.h"

#include <stdio.h>
#include <unistd.h>

void file_out(char *filename) {
    if (access(filename, F_OK) != -1) {
        FILE *file = fopen(filename, "r");

        char c, next_char;
        while ((c = fgetc(file)) != EOF) {
            if (c == '\\') {
                next_char = fgetc(file);
                if (next_char == 'n') {
                    printf("\n");
                }
            } else {
                printf("%c", c);
            }
        }
        
        fclose(file);
        printf("\n");
    } else {
        printf("n/a\n");
    }
}
