#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    // khai bao con tro p tro den mang duoc tao trong heap
    int *p = new int[n];
    // nhap du lieu cho mang 
    for(int i = 0;i<n;i++){
        cin >> p[i];
    }
    // in du lieu ra man hinh 
    for(int i = 0;i<n;i++){
        cout << p[i] << "  ";
    }
    // giai phong bo nho 
    delete [] p;
    return 0; 
}