#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int kiemTra(int &k, vector<int> &a) {
    sort(a.begin(), a.end());
    // sort(a.begin(), a.end(), greater<int>());
    return a[k - 1];
}

void xoaChan(vector<int> &a) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] % 2 == 0 && a[i] != 0) {
            a.erase(a.begin() + i);
            --i;
        }
    }
}
void showVector(vector<int> &a) {
    for (auto &i : a) {
        cout << i << " ";
    }
}

int main() {
    vector<int> a = {2, 4, 6, 8, 10};
    int k;
    // cout << "Nhap k: ";
    // cin >> k;
    // cout << kiemTra(k, a);
    xoaChan(a);
    showVector(a);
}