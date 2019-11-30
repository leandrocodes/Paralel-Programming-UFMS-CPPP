
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#define N 32

int main() {
  int values[N][N];
  int psa[N][N];
  double time = 0.0;

  // PREENCHE OS VETORES
  for (long int i = 0; i < N; i++) {
    for (long int j = 0; j < N; j++) {
      values[i][j] = 1 + rand() % 500;
      psa[i][j] = values[i][j];
    }
  }
  // PRINTA OS VETORES
  /* for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      printf("%i ", values[i][j]);
    }
    printf("\n");
  } */

  // FAZ A SOMA DOS PREFIXOS E COLETA O TEMPO

  clock_t begin = clock();
  
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      psa[i][j] =
          psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + values[i][j];
    }
  }

  clock_t end = clock();
  time += (double)(end - begin) / CLOCKS_PER_SEC;

  printf("\n ------------------------ \n");

  // PRINTA OS PREFIXOS
  /*  for (int i = 0; i < N; i++) {
     for (int j = 0; j < N; j++) {
       printf("%i ", psa[i][j]);
     }
     printf("\n");
   } */

  printf("Tempo gasto: %f ms \n", time * 1000);
}