#include <iostream>
#include <string>
using namespace std;

string input, output = "S";
int pos = 0;
string Luu[100];

void match(char c) {
    string S;
    if (c == '+')
        S = "+SS";
    else if (c == '-')
        S = "-SS";
    else
        S = "a";
    pos++;
    int posFind = output.find('S');
    if (posFind != std::string::npos) {
        output.erase(posFind, 1);
        output.insert(posFind, S);
    }
    Luu[pos] = output;
}

void S() {
    if (input[pos] == '+') {
        match('+');
        S();
        S();
    } else if (input[pos] == '-') {
        match('-');
        S();
        S();
    } else if (input[pos] == 'a') {
        match('a');
    } else {
        cout << "Syntax error " << endl;
        exit(1);
    }
}
int main() {
    cout << "Enter an input string: ";
    cin >> input;
    S();
    if (pos < input.length()) {
        cout << "Syntax error";
        exit(1);
    }
    Luu[0] = "S";
    for (int i = 0; i <= pos; i++) cout << Luu[i] << endl;
    return 0;
}