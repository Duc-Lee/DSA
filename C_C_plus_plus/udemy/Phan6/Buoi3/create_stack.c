#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    scanf("%d",&n);
    // khoi tao mang co dinh 
    int a[n];
    // ghi nhap du lieu
    for(int i = 0;i<n;i++){
        // cac phan tu duoc khai bao 
        // nam trong stack ben trong ham main
        scanf("%d",&a[i]);
    }
    // in du lieu 
    for(int i = 0;i<n;i++){
        printf("%d ",a[i]);
    }
    return 0;
}

    