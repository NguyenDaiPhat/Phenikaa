#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#define CAP 1 
using namespace std;
#include <iomanip>
void in(vector<vector<int>> &bags , vector<float> & empty_space){
    for(int i = 0; i < bags.size();i++){
        cout << 1- empty_space[i] << " - ";
        for( auto x : bags[i] ){
            
            cout << x << " " ;
        }
        cout << endl;
    }
}
void next_fit(vector<float> &w,vector<vector<int>>& bags,vector<float> &empty_space){
    bags.push_back({});
    empty_space.push_back(CAP);
    for(int itemID = 0; itemID <w.size(); itemID++){
        float canNang=w[itemID];
        if(canNang > empty_space[bags.size()-1]){
            bags.push_back({});
            empty_space.push_back(CAP);
        }
        bags[bags.size()-1].push_back(itemID);
        empty_space[bags.size()-1]-= canNang;
    }
}

void first_fit(vector<float> &w,vector<vector<int>>& bags,vector<float> &empty_space){
    bags.push_back({});
    empty_space.push_back(CAP);
    for(int itemID = 0; itemID <w.size(); itemID++){
        float canNang=w[itemID];

        int id_tui_fit =-1;
        for(int tui=0; tui < bags.size(); tui++){
            if( canNang <= empty_space[tui]){
                id_tui_fit = tui;
                break;
            }
        }

        if(id_tui_fit ==-1){
             bags.push_back({});
            empty_space.push_back(CAP);
            id_tui_fit= bags.size()-1;
        }
        if(canNang > empty_space[bags.size()-1]){
            bags.push_back({});
            empty_space.push_back(CAP);
        }
        bags[id_tui_fit].push_back(itemID);
        empty_space[id_tui_fit]-= canNang;
    }

}

void best_fit(vector<float> &w,vector<vector<int>>& bags,vector<float> &empty_space){
    bags.push_back({});
    empty_space.push_back(CAP);
    for(int itemID = 0; itemID <w.size(); itemID++){
        float canNang=w[itemID];

        int id_tui_fit =-1;
        int emptymin=99;
        for(int tui=0; tui < bags.size(); tui++){
            if( canNang <= empty_space[tui]){
                if(empty_space[tui] < emptymin){
                    emptymin=empty_space[tui];
                    id_tui_fit = tui;
                }
                
            }
        }

        if(id_tui_fit ==-1){
             bags.push_back({});
            empty_space.push_back(CAP);
            id_tui_fit= bags.size()-1;
        }
        if(canNang > empty_space[bags.size()-1]){
            bags.push_back({});
            empty_space.push_back(CAP);
        }
        bags[id_tui_fit].push_back(itemID);
        empty_space[id_tui_fit]-= canNang;
    }

}

void ffd(vector<float> &w,vector<vector<int>>& bags,vector<float> &empty_space){
    vector<pair<float,int>> items;
    for(int i=0;i<w.size();i++){
        items.push_back(make_pair(w[i],i));
    }
    sort(items.begin(), items.end(), greater<pair<float,int>>());
    bags.push_back({});
    empty_space.push_back(CAP);
    for(auto item : items){
        float canNang = item.first;
        int id_tui_fit =-1;
        int emptymin=99;
        for(int tui=0; tui < bags.size(); tui++){
            if( canNang <= empty_space[tui]){
                if(empty_space[tui] < emptymin){
                    emptymin=empty_space[tui];
                    id_tui_fit = tui;
                }
                
            }
        }

        if(id_tui_fit ==-1){
             bags.push_back({});
            empty_space.push_back(CAP);
            id_tui_fit= bags.size()-1;
        }
        if(canNang > empty_space[bags.size()-1]){
            bags.push_back({});
            empty_space.push_back(CAP);
        }
        bags[id_tui_fit].push_back(item.second);
        empty_space[id_tui_fit]-= canNang;
    }
}
int main(int argc, char* argv[]){
    vector<float> w = {0.5,0.6,0.3,0.8,0.9,0.1,0.5,0.4,0.3,0.7,0.5,0.2};
    vector<vector<int>> bags;
    vector<float> empty_space;
    //first_fit(w, bags, empty_space);
    ffd(w, bags, empty_space);
    in(bags, empty_space);

    return 0;
}