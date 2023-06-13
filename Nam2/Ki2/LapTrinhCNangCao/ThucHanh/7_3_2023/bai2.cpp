#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
    string path;
    int nodeId;
    double w;
    for (int i = 1; i < argc; ++i) {
        if (string(argv[i]) == string("-p"))
            path = argv[++i];
        if (string(argv[i]) == string("-id"))
            path = stoi(argv[++i]);
        if (string(argv[i]) == string("-w"))
            w = stod(argv[++i]);
    }
    ifstream inFile;
    inFile.open(path);
    if (!inFile.is_open()) {
        cout << "unalbe open file";
        exit;
    }
    string line;
    getline(inFile, line);
    ofstream outFile;
    outFile.open("output.txt");
    while (getline(inFile, line)) {
        int num;
        string token;
        istringstream iss(line);
        getline(iss, token, ',');
        num = stoi(token);
        if (num == nodeId) {
            getline(iss, token, ',');
            int num1 = stoi(token);
            float num2 = stod(token);
            if (num1 > w) {
                cout << nodeId << " " << num1 << " " << num2 << endl;
                outFile.
            }
        }
    }
}