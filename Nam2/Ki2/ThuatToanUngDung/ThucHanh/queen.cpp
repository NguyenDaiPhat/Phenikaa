#include <cstdlib>
#include <iostream>

using namespace std;

const int N = 100;

int n, ans;
int col[N], d1[2 * N], d2[2 * N], row[N];

void printBoard() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (row[i] == j) {
                cout << "Q ";
            } else {
                cout << ". ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

void search(int y) {
    if (y == n) {
        ans++;
        printBoard();
        return;
    }
    for (int x = 0; x < n; x++) {
        if (col[x] || d1[x + y] || d2[x - y + n - 1]) continue;
        col[x] = d1[x + y] = d2[x - y + n - 1] = 1;
        row[y] = x;
        search(y + 1);
        col[x] = d1[x + y] = d2[x - y + n - 1] = 0;
    }
}
int main() {
    cin >> n;
    search(0);
    cout << "Total solutions: " << ans << endl;
    return 0;
}
