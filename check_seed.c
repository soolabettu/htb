#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *file = fopen("random_numbers.txt", "w");
    if (file == NULL) {
        printf("Error: Unable to open file.\n");
        return 1;
    }

    for (int i = 33; i < 127; i++) {
        srand(i);
        int random_number = rand();
        fprintf(file, "%c, %d\n", i, random_number);
    }

    fclose(file);
    printf("Random numbers have been written to random_numbers.txt\n");
    return 0;
}
