#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main() {
    string s = "Hello da vagn";
    string a;
    stringstream ss(a);
    ss >> a;
    ss >> a;
    ss >> a;
    for (auto &c : s) {
        if (islower(c)) {
            c = toupper(c);
            cout << c << endl;
        }
    }
    cout << a << endl;

    return 0;
}