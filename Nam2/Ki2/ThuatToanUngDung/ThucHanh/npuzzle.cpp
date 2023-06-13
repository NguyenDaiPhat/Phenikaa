#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
#define N 3
using namespace std;
typedef vector<vector<int>> Board;

struct State {
    int x, y;
    Board board;
    vector<char> history_actions;

    vector<char> getAction() {
        // {'l','r','u','d'}
        vector<char> actions = {'l', 'r', 'u', 'd'};
        if (x == 0) {
            actions.erase(remove(actions.begin(), actions.end(), 'd'), actions.end());  // xoa 'd' trong actions
        } else if (x == N - 1) {
            actions.erase(remove(actions.begin(), actions.end(), 'u'), actions.end());  // xoa 'u' trong actions
        }

        if (y == 0) {
            actions.erase(remove(actions.begin(), actions.end(), 'r'), actions.end());  // xoa 'r' trong actions
        } else if (y == N - 1) {
            actions.erase(remove(actions.begin(), actions.end(), 'l'), actions.end());  // xoa 'l' trong actions
        }
        return actions;
    }

    void do_action(char ac) {
        history_actions.push_back(ac);
        if (ac == 'r') {
            swap(board[x][y], board[x][y - 1]);
            y--;
        } else if (ac == 'l') {
            swap(board[x][y], board[x][y + 1]);
            y++;
        } else if (ac == 'u') {
            swap(board[x][y], board[x + 1][y]);
            x++;
        } else {  // 'd'
            swap(board[x][y], board[x - 1][y]);
            x--;
        }
    }
    State() {
        for (int i = 0; i < N; i++) b.push_back(vector<int>(N, 0));
        domain_count = vector<int>(n, 0);
        for (int)
    }
    string getString() {
        string s;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; ++j) {
                s += to_string(board[i][j]);
            }
        }
        return s;
    }
};

Solution get_best_neighbor(Solition& s) {
    int bestScore = s.getScore();
    for (int cot = 0; cot < N; ++cot) {
        int hang_old = s.position[cot];
        for (int hang = 0; hang < N; ++hang){
            if(hang )
        }
    }
}

void inBoard(){
    cout<<"Score: "<< getScore()<<
}

State taoStateCon(State s, char action) {
    State stateCon = s;          // tao copy
    stateCon.do_action(action);  // perform action len state
    return stateCon;
}

bool found_in_memory(unordered_set<string>& memory, State& con) {
    string s = con.getString();
    if (memory.find(s) == memory.end())
        return false;
    else
        return true;
}

void solve(Board start, Board goal) {
    State startState = {2, 2, start};
    vector<State> pending_states = {startState};

    while (pending_states.size() > 0) {
        auto state = pending_states[0];
        if (state.board == goal) {
            cout << "OK" << endl;
            for (auto a : state.history_actions)
                cout << a << endl;
            return;
        }
        vector<char> actions = state.getAction();
        unordered_set<string> memory;
        for (char action : actions) {
            State stateCon = taoStateCon(state, action);
            if (found_in_memory(memory, stateCon))
                continue;
            pending_states.push_back(stateCon);
        }
        pending_states.erase(pending_states.begin());
    }
}

int main(int argc, char* argv[]) {
    Board start = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}};

    Board goal = {
        {1, 2, 3},
        {4, 0, 5},
        {7, 8, 6}};

    solve(start, goal);
    return 0;
}
