#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr = (int*) malloc(11 * sizeof(int));
    int *ptr = (int*) realloc(ptr, 22 * sizeof(int));
    free(ptr);
    return 0;
}
