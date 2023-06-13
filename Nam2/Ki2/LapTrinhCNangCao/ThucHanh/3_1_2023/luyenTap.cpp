#include <math.h>
#include <iostream>
#include <vector>
using namespace std;
struct Player {
    string ten;
    float cao;
    float canNang;
    int tuoi;
    int score;
    float getBmi() {
        return canNang / (cao * cao);
    }
};

int sum(vector<int> a) {
    int res = 0;
    for (int i = 0; i < a.size(); i++) {
        res += a.at(i);
    }
    return res;
}

int main() {
    vector<Player> a;
    Player x;
    int n;
    cout << "Nhap so luong cau thu: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        printf("Nhap ten cau thu %d: ", i + 1);
        cin.ignore();
        getline(cin, x.ten);
        cout << "Nhap so ban thang : ";
        cin >> x.score;
        a.push_back(x);
    }
    int MAX = 0;
    for (int i = 0; i < n; i++){
        if (MAX < a[i].score) MAX = a[i].score;
    }
    for (int i = 0; i < n; i++) {
        if (MAX == a[i].score) cout<< a[i].ten<< "\n";
    }
    return 0;
}