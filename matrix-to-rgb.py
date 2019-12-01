# -*- coding: utf-8 -*-
"""T3 PP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FAC6m5RoeRkvNsMAyOP8riS176byJjER

Installation Setup
"""

# Commented out IPython magic to ensure Python compatibility.
#!pip install git+git://github.com/andreinechaev/nvcc4jupyter.git
# %load_ext nvcc_plugin

"""# Algoritmo Sequencial"""

# Commented out IPython magic to ensure Python compatibility.
# %%cu
# 
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <unistd.h>
# #define N 4
# 
# int main() {
#   int values[N][N];
#   int reverseValues[N][N];
#   int ssa[N][N];
#   int psa[N][N];
#   double time = 0.0;
# 
#   // PREENCHE OS VETORES
#   for (long int i = 0; i < N; i++) {
#     for (long int j = 0; j < N; j++) {
#       values[i][j] = 1 + rand() % 500;
#       psa[i][j] = values[i][j];
#     }
#   }
#   // PRINTA OS VETORES
#   /* for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       printf("%i ", values[i][j]);
#     }
#     printf("\n");
#   } */
# 
#   // FAZ A SOMA DOS PREFIXOS E COLETA O TEMPO
# 
#   clock_t begin = clock();
#   
#   for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       psa[i][j] =
#           psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + values[i][j];
#     }
#   }
# 
#   clock_t end = clock();
#   time += (double)(end - begin) / CLOCKS_PER_SEC;
# 
#   // PRINTA OS PREFIXOS
#   /*  for (int i = 0; i < N; i++) {
#      for (int j = 0; j < N; j++) {
#        printf("%i ", psa[i][j]);
#      }
#      printf("\n");
#    } */
# 
#   printf("Prefixos: %f ms \n", time * 1000);
# 
#   clock_t start = clock();
# 
#   for (int i = N; i > N; i--) {
#     for (int j = N; j > N; j--) {
#       reverseValues[i][j] = values[i][j];
#     }
#   }
# 
#   for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + reverseValues[i][j];
#     }
#   }
# 
#    for (int i = N; i > N; i--) {
#     for (int j = N; j > N; j--) {
#       ssa[i][j] = psa[i][j];
#     }
#   }
#   
#   clock_t finish = clock();
#   time += (double)(finish - start) / CLOCKS_PER_SEC;
# 
#    printf("Sufixos: %f ms \n", time * 1000);
# 
# }

"""# Algoritmo Paralelo"""

# Commented out IPython magic to ensure Python compatibility.
# %%cu
# #include <thrust/generate.h>
# #include <thrust/host_vector.h>
# #include <thrust/scan.h>
# #include <iostream>
# #define D 4
# 
# __host__ static __inline__ int randFill() { return (rand() % 501); }
# 
# int main() {
#     
#   thrust::host_vector<int> hostA(D*D);
#   thrust::host_vector<int> hostB(D*D);
#   int matrixA[D][D];
#   int matrixB[D][D];
#   int index = 0;
# 
#   // INITIALIZE
#   thrust::generate(hostA.begin(), hostA.end(), randFill);
#   thrust::generate(hostB.begin(), hostB.end(), randFill);
# 
#   thrust::device_vector<int> deviceA = hostA;
#   thrust::device_vector<int> deviceB = hostB;
#   thrust::device_vector<int> deviceC(D*D);
#   
#   std::cout << "\nHost A: ";
#   for (int i = 0; i < D*D; i++){
#     std::cout << hostA[i] << " ";
#   }
#   std::cout << "\n";
#   std::cout << "Host B: ";
# 
#   for (int i = 0; i < D*D; i++){
#     std::cout << hostB[i] << " ";
#   }
#   std::cout << "\n" << std::endl;
# 
#   
#   
#   double time = 0.0;
#   clock_t begin = clock();
# 
#   thrust::inclusive_scan(deviceA.begin(), deviceA.end(), deviceA.begin());
#   
#   clock_t end = clock();
#   time += (double)(end - begin) / CLOCKS_PER_SEC;
# 
#   std::cout << "Prefixed Host A: ";
#   for (int i = 0; i < D*D; i++){
#     std::cout << deviceA[i] << " ";
#   }
# 
#   printf("\nTempo gasto: %f ms \n", time * 1000);
# 
#   // THRUST ARRAY TO MATRIX
#   for (int i = 0; i < D; i++){
#     for (int j = 0; j < D; j++){
#       matrixA[i][j] = hostA[index];
#       matrixB[i][j] = hostB[index];   
#       index++;
#     }
#   }
#   index = 0;
# 
#   // PRINT MATRIX 
# 
#   /* std::cout << "\nFinal Matrix: " << std::endl;
#   for (int i = 0; i < D; i++){
#     for (int j = 0; j < D; j++){
#         std::cout << matrixA[i][j] << " ";
#     }
#   }
#   std::cout << "\n";
# 
#   for (int i = 0; i < D; i++){
#     for (int j = 0; j < D; j++){
#         std::cout << matrixB[i][j] << " ";
#     }
#   } */
# 
#   
#   std::cout << std::endl;
#   
#   return 0;
# }