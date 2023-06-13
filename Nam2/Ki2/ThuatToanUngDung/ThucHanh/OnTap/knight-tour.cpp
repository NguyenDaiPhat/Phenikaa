#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#define N 6
using namespace std;
typedef vector<vector<int>> Board;

void in_Board(Board &b){
    for(int i=0;i<9;++i){
        for(int j=0;j<9;++j){
            cout << b[i][j] << "  ";
        }
        cout << endl;
    }
}

vector<pair<int,int>> get_possible_moves(Board &b, int h, int c){
    vector<int> x={2,-2,2,-2,1,-1,1,-1};
    vector<int> y={1,1,-1,-1,2,2,-2,-2};
    vector<pair<int,int>>moves;
    for(int i=0;i<x.size();++i){
        int newH=h+x[i];
        int newC=c+y[i];

        if(b[newH][newC]!=0  || newH >=N || newH < 0 || newC < 0 || newC >=N){
            continue;
        }
        moves.push_back(make_pair(newH,newC));
    }
    return moves;
}

bool jump(Board &b, int h,int c,int count){
    if(count> N*N){
        cout << "OK" <<endl;
        in_Board(b);
        return true;
    }
    b[h][c]=count;
     cout <<"12";
    vector<pair<int,int>>moves = get_possible_moves(b,h,c);
    for(auto move : moves){
      cout <<"1";
      bool thanhCong=jump(b,move.first,move.second,count+1);
        if(!thanhCong){
            b[move.first][move.second]=0;
        }else{
            return true;
        }
    }
    return false;
}
void solve(Board b){
    // b[0][0]=1;
    jump(b,0,0,1);
}
int main(){
    Board b;
    for(int i=0;i<N;i++){
        vector<int>v;
        for(int j=0;j<N;j++){
           v.push_back(0);
        }
        b.push_back(v);
    }
    solve(b);
    return 0;
}