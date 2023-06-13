#include <cctype>
#include <iostream>
using namespace std;
void DoThiChuyen(int& i, string& s) {
    if (s[i] == '<') {
        if (s[i + 1] == '=') {
            i++;
            cout << "quanheLE ";
        } else if (s[i + 1] == '>') {
            i++;
            cout << "quanheNE ";
        } else {
            cout << "quanheLT ";
        }
    } else if (s[i] == '=') {
        cout << "quanheEQ ";
    } else if (s[i] == '>') {
        if (s[i + 1] == '=') {
            i++;
            cout << "quanheGE ";
        } else {
            cout << "quanheGT ";
        }
    } else if (isalpha(s[i])) {
        while (isalpha(s[i + 1]) || isdigit(s[i + 1])) {
            i++;
        }
        cout << "ten ";
    } else if (isdigit(s[i])) {
        cout << "so ";
    } else if (s[i] == ' ') {
    } else
        cout << s[i] << ' ';
}
int main() {
    string s;
    cout << "Nhap du lieu can phan tich: ";
    getline(cin, s);
    int i = 0;
    while (i < s.length()) {
        DoThiChuyen(i, s);
        i++;
    }
    return 0;
}