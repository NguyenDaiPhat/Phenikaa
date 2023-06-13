// Viết hàm nhận string s làm tham số. Kiểm tra xem s có phải là một dãy IP hợp lệ.
// VD:
// 1.1.1.1, 192.168.1.24 hợp lệ
// 1.1.1.2.3, 1..2.1, 1..1.1.1, 192.300.1.2 không hợp lệ
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
bool check(string s) {
    if (s[0] < '0' || s[0] > '9') return false;
    int dem = 0, dem1 = 0;
    string s1;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '.') dem++;
        if (s[i] == '.' && s[i + 1] == '.') return false;
    }
    if (dem != 3) return false;
    // cout << dem<<" ";
    istringstream iss(s);
    while (getline(iss, s1, '.')) {
        int tam = stoi(s1);
        if (tam > 255) return false;
        // cout << s1 << " ";
        dem1++;
    }
    if (dem1 != 4) return false;
    // cout << dem1;
    return true;
}
int main() {
    string s;
    cout << "Nhap 1 day ip: ";
    cin >> s;
    // cout << s[0];
    // if (s[0] < 0 || s[0] > 9) cout << ".";
    if (check(s))
        cout << "Day la day ip hop le";
    else
        cout << "Day khong phai day ip hop le";
}