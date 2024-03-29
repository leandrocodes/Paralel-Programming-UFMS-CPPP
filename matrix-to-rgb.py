# -*- coding: utf-8 -*-
"""T3 PP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FAC6m5RoeRkvNsMAyOP8riS176byJjER

Installation Setup
"""

# Commented out IPython magic to ensure Python compatibility.
!pip install git+git://github.com/andreinechaev/nvcc4jupyter.git
# %load_ext nvcc_plugin

"""# Algoritmo Sequencial"""

# Commented out IPython magic to ensure Python compatibility.
# %%cu
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <unistd.h>
# #include <iostream>
# #define N 512
# template <typename T>
# int compare(const void* pa, const void* pb) {
#   const T& a = *static_cast<const T*>(pa);
#   const T& b = *static_cast<const T*>(pb);
#   return (a > b) - (b > a);
# }
# 
# template <typename T>
# void qsort(T* pa, std::size_t sz) {
#   if (pa) std::qsort(pa, sz, sizeof(T), compare<T>);
# }
# 
# int main() {
#   int values[N][N];
#   int reverseValues[N][N];
#   int ssa[N][N];
#   int psa[N][N];
#   int arc[N][N];
#   double time = 0.0;
# 
#   // ------------------------- PREENCHE OS VETORES -------------------------
#   for (long int i = 0; i < N; i++) {
#     for (long int j = 0; j < N; j++) {
#       values[i][j] = 1 + rand() % 500;
#       psa[i][j] = values[i][j];
#     }
#   }
#   // ------------------------- PRINTA OS VETORES -------------------------
#   /* for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       printf("%i ", values[i][j]);
#     }
#     printf("\n");
#   } */
# 
#   // ------------------------- SOMA DE PREFIXOS -------------------------
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
#   // ------------------------- SOMA DE SUFIXOS -------------------------
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
#       psa[i][j] = psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] +
#                   reverseValues[i][j];
#     }
#   }
# 
#   for (int i = N; i > N; i--) {
#     for (int j = N; j > N; j--) {
#       ssa[i][j] = psa[i][j];
#     }
#   }
# 
#   clock_t finish = clock();
#   time += (double)(finish - start) / CLOCKS_PER_SEC;
# 
#   printf("Sufixos: %f ms \n", time * 1000);
# 
#   // ------------------------- C = A + B -------------------------
# 
#   time = 0.0;
#   clock_t starting = clock();
# 
#   for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       arc[i][j] = psa[i][j] + ssa[i][j];
#     }
#   }
# 
#   clock_t finishing = clock();
#   time += (double)(finishing - starting) / CLOCKS_PER_SEC;
# 
#   printf("C = A+B: %f ms \n", time * 1000);
# 
#   // ------------------------- Quicksort -------------------------
# 
#   time = 0.0;
#   clock_t started = clock();
# 
#   for (std::size_t i = 0; i < N; ++i) qsort(arc[i], N);
# 
#   clock_t finished = clock();
#   time += (double)(finished - started) / CLOCKS_PER_SEC;
# 
#   printf("C Quicksorted: %f ms \n", time * 1000);
# 
#   // ------------------------- RGB -------------------------
# 
#   time = 0.0;
#   clock_t s = clock();
# 
#   int rgbMatrix[N][N];
#   int aux = 0;
# 
#   for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       if (arc[i][j] % 2 == 0) {
#         do {
#           aux = rand() % 256;
#         } while (aux % 2 != 0);
# 
#         rgbMatrix[i][j] = aux;
# 
#       } else {
#         do {
#           aux = rand() % 256;
#         } while (aux % 2 == 0);
#         rgbMatrix[i][j] = aux;
#       }
#     }
#   }
# 
#   clock_t f = clock();
#   time += (double)(f - s) / CLOCKS_PER_SEC;
# 
#   /* for (int i = 0; i < N; i++) {
#     for (int j = 0; j < N; j++) {
#       std::cout << rgbMatrix[i][j] << " ";
#     }
#   } */
# 
#   printf("rgbMatrix: %f ms \n", time * 1000);
# }

"""# Algoritmo Paralelo"""

# Commented out IPython magic to ensure Python compatibility.
# %%cu
# #include <thrust/device_vector.h>
# #include <thrust/for_each.h>
# #include <thrust/functional.h>
# #include <thrust/generate.h>
# #include <thrust/host_vector.h>
# #include <thrust/iterator/zip_iterator.h>
# #include <thrust/scan.h>
# #include <thrust/sort.h>
# #include <iostream>
# #define D 512
# 
#         __host__ static __inline__ int
#         randFill() {
#   return (rand() % 501);
# }
# 
# __host__ static __inline__ int
#         randRGB() {
#   return (rand() % 256);
# }
# 
# struct arbitrary_functor {
#   template <typename Tuple>
#   __host__ __device__ void operator()(Tuple t) {
#     thrust::get<0>(t) = thrust::get<1>(t) + thrust::get<2>(t);
#   }
# };
# 
# int main() {
#   thrust::host_vector<int> hostA(D * D);
#   thrust::host_vector<int> hostB(D * D);
#   thrust::host_vector<int> hostRGB(D * D);
#   int matrixA[D][D];
#   int matrixB[D][D];
#   int index = 0;
# 
#   // ------------------------- INITIALIZE -------------------------
#   thrust::generate(hostA.begin(), hostA.end(), randFill);
#   thrust::generate(hostB.begin(), hostB.end(), randFill);
# 
#   thrust::device_vector<int> deviceA = hostA;
#   thrust::device_vector<int> deviceB = hostB;
#   thrust::device_vector<int> deviceC(D * D);
# 
#   /* std::cout << "\nHost A: ";
#   for (int i = 0; i < D * D; i++) {
#     std::cout << hostA[i] << " ";
#   }
#   std::cout << "\n";
#   std::cout << "Host B: ";
# 
#   for (int i = 0; i < D * D; i++) {
#     std::cout << hostB[i] << " ";
#   }
#   std::cout << "\n" << std::endl; */
# 
#   // ------------------------- SOMA DE PREFIXOS -------------------------
#   double time = 0.0;
#   clock_t begin = clock();
# 
#   thrust::inclusive_scan(deviceA.begin(), deviceA.end(), deviceA.begin());
# 
#   clock_t end = clock();
#   time += (double)(end - begin) / CLOCKS_PER_SEC;
# 
#   /*std::cout << "Prefixed Device A: ";
#   for (int i = 0; i < D * D; i++) {
#     std::cout << deviceA[i] << " ";
#   }*/
# 
#   printf("Prefixos: %f ms \n", time * 1000);
# 
#   // ------------------------- SOMA DE SUFIXOS -------------------------
#   time = 0.0;
#   clock_t start = clock();
# 
#   thrust::stable_sort(deviceB.begin(), deviceB.end(), thrust::greater<int>());
# 
#   thrust::inclusive_scan(deviceB.begin(), deviceB.end(), deviceB.begin());
# 
#   thrust::stable_sort(deviceB.begin(), deviceB.end(), thrust::greater<int>());
# 
#   clock_t finish = clock();
#   time += (double)(finish - start) / CLOCKS_PER_SEC;
# 
#   /*std::cout << "\nSufixed Device B: ";
#   for (int i = 0; i < D * D; i++) {
#     std::cout << deviceB[i] << " ";
#   }*/
# 
#   printf("Sufixos: %f ms \n", time * 1000);
# 
#   // ------------------------- C = A+B -------------------------
# 
#   time = 0.0;
#   clock_t starting = clock();
# 
#   thrust::for_each(thrust::make_zip_iterator(thrust::make_tuple(
#                        deviceC.begin(), deviceA.begin(), deviceB.begin())),
#                    thrust::make_zip_iterator(thrust::make_tuple(
#                        deviceC.end(), deviceA.end(), deviceB.end())),
#                    arbitrary_functor());
# 
#   clock_t finishing = clock();
#   time += (double)(finishing - starting) / CLOCKS_PER_SEC;
# 
#   /*std::cout << "\nC = A+B: ";
#   for (int i = 0; i < D * D; i++) {
#     std::cout << deviceC[i] << " ";
#   }*/
# 
#   printf("C = A+B: %f ms \n", time * 1000);
# 
#   // ------------------------- Quicksort C -------------------------
# 
#   time = 0.0;
#   clock_t started = clock();
# 
#   thrust::sort(deviceC.begin(), deviceC.end());
# 
#   clock_t finished = clock();
#   time += (double)(finished - started) / CLOCKS_PER_SEC;
# 
#   /*std::cout << "\nQuicksorted C: ";
#   for (int i = 0; i < D * D; i++) {
#     std::cout << deviceC[i] << " ";
#   }*/
# 
#   printf("Quicksorted C: %f ms \n", time * 1000);
# 
#   // ------------------------- RGB Array2d -------------------------
# 
#   time = 0.0;
#   clock_t s = clock();
# 
#   //thrust::generate(hostRGB.begin(), hostRGB.end(), randRGB);
#   thrust::device_vector<int> deviceRGB = hostRGB;
#   
#   clock_t f = clock();
#   time += (double)(f - s) / CLOCKS_PER_SEC;
# 
#   
# 
#   printf("RGB 2dArray: %f ms \n", time * 1000);
# 
#   // ------------------------- TRANSFORMA EM MATRIZ DENOVO
#   // -------------------------
#   for (int i = 0; i < D; i++) {
#     for (int j = 0; j < D; j++) {
#       matrixA[i][j] = hostA[index];
#       matrixB[i][j] = hostB[index];
#       index++;
#     }
#   }
#   index = 0;
# 
#   // ------------------------- PRINT MATRIX -------------------------
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
#   std::cout << std::endl;
# 
#   return 0;
# }