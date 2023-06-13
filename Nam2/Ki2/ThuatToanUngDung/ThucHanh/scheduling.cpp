#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main(int argc, char* agrv[]) {
    string s = "1, 2, 3, 4, 5, 6, 8 ";
    stringstream iss;
    iss << s;
    int num, sum = 0;
    string s1;
    // while (getline(iss, s1, ',')) {
    //     num = stoi(s1);
    //     sum += num;
    // }
    iss >> s1;
    sum += stoi(s1);
    cout << sum << endl;

    ostringstream oss;
    oss << "hello";
    oss << " abc\n";
    string ss = oss.str();
    cout << ss << "\n";
    return 0;
}
