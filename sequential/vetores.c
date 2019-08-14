#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main(){
    long int a[1000000];
    long int b[1000000];
    long int c[1000000];


    double time = 0.0;

    for (long int i = 0; i < 1000000; i++){
        a[i] = i;   
        b[i] = i;
    }

    clock_t begin = clock();
    for (long int i = 0; i < 1000000; i++){
        c[i] = a[i] + b[i];
    }

    clock_t end = clock();
    time += (double)(end - begin) / CLOCKS_PER_SEC;

	printf("Tempo gasto: %f segundos", time);
}