#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
#define N 8
using namespace std;
typedef vector<vector<int>> Board;

void in_Board(Board &b) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << b[i][j] << " ";
        }
        cout << endl;
    }
}

vector<int> get_possible_moves(Board &b, int h, int c) {
    vector<int> x = {-2, -2, -1, -1, 1, 1, 2, 2};
    vector<int> y = {-1, 1, -2, 2, -2, 2, -1, 1};
    vector<pair<int, int>> moves;
    for (int i = 0; i < x.size(); i++) {
        int newH = h + x[i];
        int newC = c + y[i];
        if (newH >= N || newH < 0 || newC >= N || newC < 0 || b[newH][newC])
            if (b[newH][newC] == 0) {
                moves.push_back(make_pair(newH, newC));
            }
    }
    return moves;
}

bool jump(Board &b, int h, int c, int count) {
    if (count > N * N) {
        cout << " oke" << endl;
        inBoard(b);
        return true;
    }
    vector<pair<int, int>> moves = get_possible_moves(b, h, c);
    for (auto move : moves) {
    }
}

int main() {
    Board b;
    for (int i = 0; i < N; i++) {
        vector<int> v;
        for (int j = 0; j < N; j++) {
            v.push_back(0);
        }

        return 0;
    }