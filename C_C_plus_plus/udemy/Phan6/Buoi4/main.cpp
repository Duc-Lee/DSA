#include <bits/stdc++.h>
using namespace std;

int main(){
    // khoi tao mang dong p
    // mang p co 5 phan tu
    int *p = new int[5];
    // khoi tao gia tri cho 5 phan tu 
    p[0] = 5;
    p[1] = 8;
    p[2] = 9;
    p[3] = 6;
    p[4] = 4;
    // bh mang p = {5,8,9,6,4}
    // ta muon tang mang p len 10 phan tu 
    // khoi tao con tro q 
    int *q = new int[10];
    // copy phan tu sang mang q
    for(int i = 0;i < 5;i++) {
        q[i] = p[i];
    }
    // xoa mang hien tai p dang tro di 
    delete []p;
    // gan dia chi q dang tro cho p
    p = q;
    // gan q bang null 
    q = NULL;
    // luu y : neu khong gan ma free luon  
    // q van dang tro vung nho mang 10 phan tu 
    // free luon la mang 10 phan tu bi giai phong 
    delete []q;
}