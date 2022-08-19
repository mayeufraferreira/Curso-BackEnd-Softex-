#include <stdio.h>
#include <stdlib.h>

int main() {
    int *v = (int*) malloc(11 * sizeof(int));
    *v = (int*) realloc(v, 22 * sizeof(int));
    
    for (int i = 0; i < 22; i++){
        v[i] = 2 * i;
    }
    
    for (int i = 0; i < 22; i++) {
        printf("%d\n", v[i]);
    }
    
    free(v);
}
