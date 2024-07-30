#include "filewriter.h"
#include "filehandler.h"
#include <stdio.h>
#include <unistd.h>

void file_input(char *filename, char *content) {
    FILE *file = fopen(filename, "a");
    if (file != NULL) {
        fprintf(file, "%s", content);
        fclose(file);
        file_out(filename);
    } else {
        printf("n/a\n");
    }
}
