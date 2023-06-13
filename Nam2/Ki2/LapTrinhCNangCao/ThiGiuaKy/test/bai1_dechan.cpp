#include <iostream>
#include <map>
#include<sstream>
#include<fstream>
#include<vector>
using namespace std;
void xuLy(string &s, int n)
{
    for (auto &a : s)
    {
        if (!(a >= 'a' && a<= 'z') && !(a>='A' && a <= 'Z')){
            a = ' ';
        }
    }
    map<string, int> map;
    istringstream iss(s);
    string token;
    while (iss >> token){
        map[token]++;
    }
    vector<pair<string, int>> vec(map.begin(), map.end());
    for(int i = 0; i < vec.size()-1; i++)
    for(int j = i + 1; j<vec.size(); j++)
    if(vec[i].second < vec[j].second){
        auto tg = vec[i];
        vec[i] = vec[j];
        vec[j] = tg;
    }
    for (int i = 1; i<=n;i++){
        cout<<vec[i].first<<endl;
    }
    
}
int main()
{
    string s = "haha hihi haha hihi haha kk kk kk kk vc";
    int n = 2;
    xuLy(s,n);
    return 0;
}