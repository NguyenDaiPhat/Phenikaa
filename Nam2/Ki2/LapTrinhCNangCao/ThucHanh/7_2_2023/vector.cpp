#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int n, count = 0;
    vector<int> A;
    for (int i = 0;; i++) {
        cin >> i;
        A.push_back(i);
        if (is_prime(i)) count++;
        if (count == 2) break;
    }
    for (auto i : A) {
        cout << i;
    }

    return 0;
}
