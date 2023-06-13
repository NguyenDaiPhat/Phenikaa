#include<iostream>
#include<vector>
#include<algorithm>
#define N 3;
using namespace std;

typedef vector<vector<int>> Board;

struct State
{
    int x, y;
    Board board;
    vector<char> history_actions;
    vector<char> getAction(){
        vector<char> action = {'l', 'r', 'u', 'd'};
        if(x == 0){
            action.erase(remove(action.begin(), action.end(), 'd'), action.end());//xoa d trong action
        }
        else if(x == N-1){
            action.erase(remove(action.begin(), action.end(), 'u'), action.end());//xoa u trong action
        }
        if(y == 0){
            action.erase(remove(action.begin(), action.end(), 'r'), action.end());//xoa r trong action
        }
        else if(y == N-1){
            action.erase(remove(action.begin(), action.end(), 'l'), action.end());//xoa l trong action
        }
        return action;
    }
    void do _action(char ac){
        history_actions.push_back(ac);
        if(ac == 'r'){
            swap(board[x][y], board[x][y-1]);
            y--;
        }else if(ac == 'l'){
            swap(board[x][y], board[x][y+1]);
            y--;
        }else if(ac == 'u'){
            swap(board[x][y], board[x+1][y]);
            y--;
        }else {
            swap(board[x][y], board[x-1][y]);
            y--;
        }
    }
};


void solve(Board start, Board goal){
    State startState = {2,2,start};
    vector<State> pending_states = {startState};
    while (pending_states.size() > 0){
        auto state = pending_states[0];
        if(state.board == goal){
            cout<< "OK" << endl;
            for(auto a:state.history_actions)
                cout<< a <<endl;
            return;
        }
        vector<char> actions = state.getAction();
        for (char action : actions){
            State stateCon = state;
            stateCon.do_action(action);
            pending_states.push_back(stateCon);
        }
        pending_states.erase(pending_states.begin());
    }
}

int main(int argc, char*argv[]){
    Board start = {
        {1,2,3},
        {4,5,6},
        {7,8,0}
    };
    Board goal ={
        {1,0,2},
        {4,5,3},
        {7,8,6}
    };
    solve(start, goal);
    return 0;
}