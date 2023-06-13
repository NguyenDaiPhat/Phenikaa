#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#define N 50
using namespace std;
typedef vector<vector<int>> Board;
struct State{
    Board b;
    vector<int> domain_count;
    unordered_set<int> unassigned_cols;
    State(){
        for (int i = 0; i < N;i++){
            b.push_back(vector<int>(N,0));
        }
        domain_count=vector<int>(N,0);
        for(int i = 0; i < N;i++){
            unassigned_cols.insert(i);
        }
    }


    vector<pair<int, int>> forward_checking(int h, int c){
    vector<pair<int, int>> tracks;
    // danh dau hang ngang 
    for(int cot=0;cot<N;cot++){
        if(b[h][cot] == 0) {
            b[h][cot] = -1;
            tracks.push_back(make_pair(h, cot));
            domain_count[cot]--;
        }
    }
    // danh dau cheo tren phai
    for(int i=h-1,j=c+1; i>=0 && j<N ;i--,j++){
        if(b[i][j] == 0) {
            b[i][j] = -1;
            tracks.push_back(make_pair(i, j));
            domain_count[j]--;
        }
    }

    // danh dau cheo duoi phai
    for(int i=h+1,j=c+1; i<N && j<N ;i++,j++){
        if(b[i][j] == 0) {
            b[i][j] = -1;
            tracks.push_back(make_pair(i, j));
            domain_count[j]--;
        }
    }

    // Trai 

    // danh dau cheo tren trai
    for(int i=h-1,j=c-1; i>=0 && j>=0 ;i--,j--){
        if(b[i][j] == 1) {
            b[i][j] = -1;
            tracks.push_back(make_pair(i, j));
            domain_count[j]--;
        }
    }

    // danh dau cheo duoi
    for(int i=h+1,j=c-1; i<N && j>=0 ;i++,j--){
        if(b[i][j] == 1) {
            b[i][j] = -1;
            tracks.push_back(make_pair(i, j));
            domain_count[j]--;
        }
    }
    return tracks;
}

int getNextColum(){
    int min=9999;
    int chosen_col=-1;
    for(int col : unassigned_cols){
        if(domain_count[col] < min){
            min= domain_count[col];
            chosen_col = col;
        }
    }
    return chosen_col;
}

void in_Board(){
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            if(b[i][j]==-1){
                b[i][j]=0;
            }
            cout << b[i][j] << "  ";
        }
        cout << endl;
    }
}
};

// vector<pair<int,int>> FC(Board &b, int h,int c){
//     vector<pair<int,int>> truyVet;

//     // ngang
//     for(int cot=c+1;cot<N;cot++){
//         b[h][cot] =-1;
//         truyVet.push_back(make_pair(h,cot));
//     }
//     // cheo tren 
//     for(int i=h-1,j=c+1; i>=0 && j<N ;i--,j++){
//         b[i][j]=-1;
//         truyVet.push_back(make_pair(i,j));
//     }

//     // cheo duoi 
//     for(int i=h+1,j=c+1; i<N && j<N ;i++,j++){
//         b[i][j]=-1;
//         truyVet.push_back(make_pair(i,j));
//     }
//     return truyVet;
// }




//  bool check(Board &b, int h,int c){
// //     //check hang
//         for(int j = c ;j>=0;--j){
//             if(b[h][j] == 1) return false;
//         }
//     // check cheo tren
//     for(int i = h, j = c; i>=0 && j>=0 ;--i,--j ){
//         if(b[i][j] == 1) return false;
//     }
//     for(int i = h, j = c; i<N && j>=0 ;++i,--j ){
//         if(b[i][j] == 1) return false;
//     }
//         return true;
//  }


bool them_hau_vao_cot(State &s, int cot){
    if(s.unassigned_cols.size() <= 0){
        cout << "OK"<< endl;
        s.in_Board();
        return true;
    }
    for(int hang=0;hang< N;++hang){
        if(s.b[hang][cot]==-1) continue;
            s.b[hang][cot] =1;
            s.unassigned_cols.erase(cot);
            auto tracks= s.forward_checking(hang,cot);

            bool thanhCong = them_hau_vao_cot(s,s.getNextColum());
            if(!thanhCong){
                s.b[hang][cot] =0;
                for(auto p: tracks){
                    s.b[p.first][p.second]=0;
                    s.domain_count[p.second]++;
                }
            }else{
                return true;
            }
        
    }
    s.unassigned_cols.insert(cot);
    return false;
}
bool solve(State &s){
//pair in c++
    them_hau_vao_cot(s,0);

}
int main(int argc, char* argv[]){
    State s;
    Board b;
    for(int i=0;i<N;i++){
        vector<int> v;
        for(int j=0;j<N;j++){
            v.push_back(0);
            
        }
        b.push_back(v);
    }
    
    solve(s);
    return 0;
}





















