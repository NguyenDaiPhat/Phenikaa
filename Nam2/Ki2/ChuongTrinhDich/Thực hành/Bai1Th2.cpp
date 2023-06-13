#include <cctype>
#include <iostream>
using namespace std;
int main() {
    string s;
    cout << "Nhap tu to: ";
    getline(cin, s);
    int i = 0;
    while (i < s.length()) {
        if (isalpha(s[i])) {
            while (isalpha(s[i + 1]) || isdigit(s[i + 1])) {
                i++;
            }
            if (i == s.length() - 1)
                cout << "ten ";
            else
                {
                    cout << "loi";
                    return 0;
                }
        } else {
            cout << "loi";
            return 0;
        }
        i++;
    }
    cout << s;
    return 0;
}