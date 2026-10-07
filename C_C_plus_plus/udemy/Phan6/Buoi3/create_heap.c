#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d",&n);
    // khai bao con tro tro den vung nho duoc tao trong heap
    // khoi tao ra mang dong n phan tu 
    int *p = (int*)malloc(n * sizeof(int));
    // ghi nhap du lieu vao mang 
    for(int i = 0;i<n;i++){
        scanf("%d",&p[i]);
    }
    // in du lieu ra man hinh 
    for(int i = 0;i<n;i++){
        printf("%d ",p[i]);
    }
    free(p);
    return 0;
}