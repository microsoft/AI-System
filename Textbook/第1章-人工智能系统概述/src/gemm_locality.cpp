#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int M = 3;
    int N = 3;
    int K = 3;
    int A[M][K];
    int B[K][N];
    int C[M][N];
    
    for (int m = 0; m < M; m++) {
      for (int n = 0; n < N; n++) {
        C[m][n] = 0;
        for (int k = 0; k < K; k++) {
          C[m][n] += A[m][k] * B[k][n];
          printf("%d \n", &A[m][k]);
          printf("%d \n", &B[k][n]);
          printf("%d \n", &C[m][n]);
        }
      }
    }
    return 0;
}
