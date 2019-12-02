#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <iostream>
#define N 2
template <typename T>
int compare(const void* pa, const void* pb) {
  const T& a = *static_cast<const T*>(pa);
  const T& b = *static_cast<const T*>(pb);
  return (a > b) - (b > a);
}

template <typename T>
void qsort(T* pa, std::size_t sz) {
  if (pa) std::qsort(pa, sz, sizeof(T), compare<T>);
}

int main() {
  int values[N][N];
  int reverseValues[N][N];
  int ssa[N][N];
  int psa[N][N];
  int arc[N][N];
  double time = 0.0;

  // ------------------------- PREENCHE OS VETORES -------------------------
  for (long int i = 0; i < N; i++) {
    for (long int j = 0; j < N; j++) {
      values[i][j] = 1 + rand() % 500;
      psa[i][j] = values[i][j];
    }
  }
  // ------------------------- PRINTA OS VETORES -------------------------
  /* for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      printf("%i ", values[i][j]);
    }
    printf("\n");
  } */

  // ------------------------- SOMA DE PREFIXOS -------------------------

  clock_t begin = clock();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      psa[i][j] =
          psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + values[i][j];
    }
  }

  clock_t end = clock();
  time += (double)(end - begin) / CLOCKS_PER_SEC;

  // PRINTA OS PREFIXOS
  /*  for (int i = 0; i < N; i++) {
     for (int j = 0; j < N; j++) {
       printf("%i ", psa[i][j]);
     }
     printf("\n");
   } */

  printf("Prefixos: %f ms \n", time * 1000);

  // ------------------------- SOMA DE SUFIXOS -------------------------

  clock_t start = clock();

  for (int i = N; i > N; i--) {
    for (int j = N; j > N; j--) {
      reverseValues[i][j] = values[i][j];
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] +
                  reverseValues[i][j];
    }
  }

  for (int i = N; i > N; i--) {
    for (int j = N; j > N; j--) {
      ssa[i][j] = psa[i][j];
    }
  }

  clock_t finish = clock();
  time += (double)(finish - start) / CLOCKS_PER_SEC;

  printf("Sufixos: %f ms \n", time * 1000);

  // ------------------------- C = A + B -------------------------

  time = 0.0;
  clock_t starting = clock();

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      arc[i][j] = psa[i][j] + ssa[i][j];
    }
  }

  clock_t finishing = clock();
  time += (double)(finishing - starting) / CLOCKS_PER_SEC;

  printf("C = A+B: %f ms \n", time * 1000);

  // ------------------------- Quicksort -------------------------

  time = 0.0;
  clock_t started = clock();

  for (std::size_t i = 0; i < N; ++i) qsort(arc[i], N);

  clock_t finished = clock();
  time += (double)(finished - started) / CLOCKS_PER_SEC;

  printf("C Quicksorted: %f ms \n", time * 1000);

  // ------------------------- RGB -------------------------

  time = 0.0;
  clock_t s = clock();

  int rgbMatrix[N][N];
  int aux = 0;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (arc[i][j] % 2 == 0) {
        do {
          aux = rand() % 257;
        } while (aux % 2 != 0);

        rgbMatrix[i][j] = aux;

      } else {
        do {
          aux = rand() % 257;
        } while (aux % 2 == 0);
        rgbMatrix[i][j] = aux;
      }
    }
  }

  clock_t f = clock();
  time += (double)(f - s) / CLOCKS_PER_SEC;

  /* for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      std::cout << rgbMatrix[i][j] << " ";
    }
  } */

  printf("rgbMatrix: %f ms \n", time * 1000);
}