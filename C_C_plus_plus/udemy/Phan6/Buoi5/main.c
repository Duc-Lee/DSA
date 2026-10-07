#include <stdlib.h>
#include <stdio.h>

int main(){
    // khoi tao con tro cap 2
    int **A;
    // khoi tao 3 mang con tro
    A = malloc(3 * sizeof(int*));
    // khoi tao 3 mang so nguyen
    // moi mang co 4 phan tu A[i][j] j 
    for(int i = 0;i < 3;i++) {
        A[i] = malloc(4 * sizeof(int));
    }
    // nhap mang
    for(int i = 0;i < 3;i++) {
        for(int j = 0;j < 4;j++) {
            scanf("%d",&A[i][j]);
        }
    }
    // in mang
    for(int i = 0;i < 3;i++) {
        for(int j = 0;j < 4;j++) {
            printf("%d ",A[i][j]);
        }
    }
    // giai phong bo nho
    for(int i = 0;i < 3;i++) {
        // giai phong 3 mang so nguyen
        free(A[i]);
    }
    // giai phong con tro cap 2
    free(A);
    return 0;
}