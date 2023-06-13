#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <time.h>
#include <ctime>
#include <cstdlib>
#define N 6
using namespace std;
typedef vector<vector<int>> Board;

struct Solution
{
    Board b;
    vector<int> position;
    Solution(){
        for(int i=0; i<N; i++)
            b.push_back(vector<int>(N,0));
            position=vector<int>(N,-1);
        
    }

    void placeQueen(int hang, int cot){
        int hang_old= position[cot];
        if(hang_old != -1){
            b[hang_old][cot]=0;
        }
        b[hang][cot]=1;
        position[cot]=hang;
       
    }

    void in_Board(){
        for(int i=0;i<N;++i){
            for(int j=0;j<N;++j){
                cout << b[i][j] << "  ";
            }
            cout << endl;
        }
    }

    int getScore(){
        int count = 0;
        for(int cot=0;cot<N;++cot){
            int hang= position[cot];

            // check hang ngang
            for(int j= cot+1 ; j<N;++j){
                if(b[hang][j]==1){
                    count++;
                }
            }
                // check cheo tren 
            for(int i=hang-1,j=cot+1;i >=0 && j<N;i--,j++){
                if(b[i][j]==1){
                    count++;
                }
            }

            // check cheo duoi
            for(int i=hang+1,j=cot+1;i<N&&j<N;i++,j++){
                if(b[i][j]==1){
                    count++;
                }
            }
            }

            return count;
        }

};
Solution get_best_neighbor(Solution &s){
    int bestScore=s.getScore();
    Solution bestS;
    for(int cot=0;cot<N;cot++){
        int hang_old=s.position[cot];
        for(int hang=0;hang<N;hang++){
            if(hang==hang_old)continue;
            Solution newS = s;
            newS.placeQueen(hang,cot);
            //newS.in_Board();
            int newScore= newS.getScore();
            if(newScore < bestScore){
                bestScore= newScore;
                bestS=newS;
            }
        }
    }
    return bestS;
}
void in_Board(Board &b){
    for(int i=0;i<N;++i){
        for(int j=0;j<N;++j){
            cout << b[i][j] << "  ";
        }
        cout << endl;
    }
}

int main(){
    Solution s;
    srand(time(NULL));
    for(int cot=0; cot < N;++cot){
       
        int hang_ngau_nhien= rand() % N;
        s.placeQueen(hang_ngau_nhien,cot);
    }
    //s.in_Board();
    
    int count =0;
    while(s.getScore()!=0 && count < 100){
        for(int cot=0; cot < N;++cot){
       
        int hang_ngau_nhien= rand() % N;
        s.placeQueen(hang_ngau_nhien,cot);
    }
        count ++;
        while(1){
            Solution best= get_best_neighbor(s);
            if(s.getScore()== best.getScore() ) break;
            else if(best.getScore()== 0){
                s= best;
                break;
            }
            else s= best;
        }
        cout << "1";
    }
    s.in_Board();
    cout <<"Score " << s.getScore() << endl;
    return 0;
}
