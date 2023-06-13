#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
int main(int argc, char* argv[]) {
    ifstream inFile;
    inFile.open("/PHENIKAA/Ki4/LapTrinhCNangCao/28_2_2023/QuaBongVang.txt");
    if (!inFile.is_open()) {  // inFile.fail()
        cout << "unable to open file!\n";
        exit(0);
    }
    string s1, luu;
    unordered_map<string, int> DemTu;
    while (inFile >> s1) {
        DemTu[s1]++;
    }
    int max1 = 0;
    for (auto p : DemTu) {
        // cout << p.first << " " << p.second << endl;
        if (max1 < p.second) {
            max1 = p.second;
            luu = p.first;
        }
    }
    cout << "Cau thu ghi ban nhieu nhat: " << luu;
}