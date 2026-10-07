#include <bits/stdc++.h>
using namespace std;

int main(){
    // khoi tao n 
    int n; 
    // khai bao mang tinh 
    int a[n];
    // mang nay se nam tren stack
    for(int i  = 0;i < n ;i++){
        // cac phan tu duoc khai bao
        // se nam tren stack ben trong ham main
        cin  >> a[i];
    }
    // in ra cac phan tu 
    for(int i = 0;i<n ;i++){
        cout << a[i] << "  ";
    }
    return 0; 
}