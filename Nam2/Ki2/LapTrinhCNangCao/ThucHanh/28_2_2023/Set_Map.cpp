#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
#include<unordered_map>
using namespace std;
int main(int argc, char* argv[]) {
    set<string> words;
    words.insert("a");
    words.insert("b");
    words.insert("c");
    words.insert("d");
    words.insert("e");
    // cout << *(++words.begin());
    // cout << *(++++words.begin());
    // string s = "abc def aaf k abc c";
    // string s1;
    // unordered_set<string> DemTu;
    // istringstream iss(s);
    // while (iss >> s1) {
    //     DemTu.insert(s1);
    // }
    // for(auto demtu : DemTu)
    //     cout << demtu<<" ";
    map<string, float> scores;
    scores.insert(make_pair("k", 10));
    scores.insert(make_pair("a", 20));
    scores.insert(make_pair("z", 30));
    scores.insert(make_pair("h", 50));
    scores.insert(make_pair("Z", 80));
    scores.erase("a");

    unordered_map<string, int> DemTu;
    string s = "abc def aaf k abc c";
    string s1, luu;
    istringstream iss(s);
    while (iss >> s1) {
        DemTu[s1]++;
    }
    int max1 = 0;
    for (auto p : DemTu) {
        cout << p.first << " " << p.second << endl;
        if (max1 < p.second) {
            max1 = p.second;
            luu = p.first;
        }
    }
    cout << "Phan tu xuat hien nhieu nhat " << luu;
}