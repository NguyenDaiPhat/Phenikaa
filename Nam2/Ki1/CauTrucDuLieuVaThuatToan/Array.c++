#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    int n,m;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> m;
    int b[m];
    for (int i = 0; i < m; i++) cin >> b[i];
    int size = n+m;
    int c[size];
    merge(a, a + n, b, b + m, c);
    for (int i = 0; i<size; i++){
        cout << c[i] << " ";
    }
}