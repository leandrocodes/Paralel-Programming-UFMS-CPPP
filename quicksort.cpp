#include <cstdlib>
#include <iostream>

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
  const std::size_t NROWS = 3;
  const std::size_t NCOLS = 5;
  int array[NROWS][NCOLS] = {{1, 5, 9, 2, 7}, {8, 1, 7, 4, 0}, {1, 3, 5, 4, 2}};

  for (auto& row : array) qsort(row, NCOLS);
  // for( std::size_t i = 0 ; i < NROWS ; ++i ) qsort( array[i], NCOLS ) ;

  for (auto& row : array) {
    for (int v : row) std::cout << v << ' ';
    std::cout << '\n';
  }
}