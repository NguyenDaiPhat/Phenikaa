#include <math.h>

#include <iostream>
using namespace std;
void ktsnt(int &n) {
    if (n < 2) {
        n++;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            n++;
        }
    }
    n = n * 2;
    cout << n;
}
double thetich(float h, float r){
    return h * r * r * 3.14;
}
int main() {
    // int n;
    // cin >> n;
    // ktsnt(n);
    const float pi = 3.14;
    int r, h;
    cin >> r >> h;
    cout << thetich(h, r);
    return 0;
}