#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
#define N 9
using namespace std;
typedef vector<vector<int>> Board;

void in_Board(Board &b) {
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            cout << b[i][j] << "  ";
        }
        cout << endl;
    }
}
bool check(Board &b, int cot, int hang, int val) {
    for (int i = 0; i < 9; ++i) {
        if (b[i][cot] == val) {
            return false;
        }
        if (b[hang][i] == val) {
            return false;
        }
    }
    hang = hang / 3;
    cot = cot / 3;
    hang = hang * 3;
    cot = cot * 3;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; j++) {
            if (b[hang + i][cot + j] == val) {
                return false;
            }
        }
    }
    return true;
}
bool fill_cell(Board &b, vector<int> empty_cells, int index) {
    if (index >= empty_cells.size()) {
        cout << "OK" << endl;
        in_Board(b);
        return true;
    }
    int id = empty_cells[index];
    int hang = id / 9;
    int cot = id % 9;
    if (b[hang][cot] != 0) {
        fill_cell(b, empty_cells, index + 1);
    } else {
        for (int i = 1; i <= N; i++) {
            if (check(b, cot, hang, i)) {
                b[hang][cot] = i;
                if (!fill_cell(b, empty_cells, index + 1)) {
                    b[hang][cot] = 0;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}
void solve(Board b) {
    vector<int> empty_cells;
    for (int id = 0; id < N * N; id++) {
        int hang = id / 9;
        int cot = id % 9;
        if (b[hang][cot] == 0) {
            empty_cells.push_back(id);
        }
    }
    fill_cell(b, empty_cells, 0);
}
int main() {
    Board b = {
        {0, 2, 0, 0, 6, 0, 0, 0, 9},
        {0, 0, 7, 4, 0, 2, 0, 0, 3},
        {0, 0, 0, 0, 8, 0, 4, 0, 0},
        {0, 9, 0, 2, 0, 3, 1, 0, 0},
        {0, 0, 8, 0, 0, 0, 0, 9, 0},
        {0, 0, 0, 0, 0, 6, 0, 0, 0},
        {0, 8, 0, 1, 0, 9, 3, 0, 0},
        {5, 0, 0, 0, 0, 0, 0, 0, 7},
        {0, 0, 0, 0, 4, 0, 0, 0, 0}};
    solve(b);
    return 0;
}