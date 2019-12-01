#include <thrust/generate.h>
#include <thrust/host_vector.h>
#include <thrust/scan.h>
#include <iostream>
#define D 2

__host__ static __inline__ int randFill() { return (rand() % 501); }

int main() {
  thrust::host_vector<int> hostA(D * D);
  thrust::host_vector<int> hostB(D * D);
  thrust::device_vector<int> deviceC(D * D);
  int matrixA[D][D];
  int matrixB[D][D];
  int index = 0;

  // INITIALIZE
  thrust::generate(hostA.begin(), hostA.end(), randFill);
  thrust::generate(hostB.begin(), hostB.end(), randFill);

  std::cout << "\nHost A: ";

  for (int i = 0; i < D * D; i++) {
    std::cout << hostA[i] << " ";
  }
  
  std::cout << "\n";
  std::cout << "Host B: ";
  
  for (int i = 0; i < D * D; i++) {
    std::cout << hostB[i] << " ";
  }
  
  std::cout << "\n" << std::endl;

  int data[D * D];

  for (int i = 0; i < D * D; i++) {
    data[i] = hostA[i];
  }

  double time = 0.0;
  clock_t begin = clock();

  thrust::inclusive_scan(data, data + D * D, data);

  clock_t end = clock();
  time += (double)(end - begin) / CLOCKS_PER_SEC;

  std::cout << "Prefixed Host A: ";

  for (int i = 0; i < D * D; i++) {
    std::cout << data[i] << " ";
  }

  printf("\nTempo gasto: %f ms \n", time * 1000);

  // THRUST ARRAY TO MATRIX
  for (int i = 0; i < D; i++) {
    for (int j = 0; j < D; j++) {
      matrixA[i][j] = hostA[index];
      matrixB[i][j] = hostB[index];
      index++;
    }
  }
  index = 0;

  // PRINT MATRIX

  /* std::cout << "\nFinal Matrix: " << std::endl;
  for (int i = 0; i < D; i++){
    for (int j = 0; j < D; j++){
        std::cout << matrixA[i][j] << " ";
    }
  }
  std::cout << "\n";

  for (int i = 0; i < D; i++){
    for (int j = 0; j < D; j++){
        std::cout << matrixB[i][j] << " ";
    }
  } */

  std::cout << std::endl;

  return 0;
}
