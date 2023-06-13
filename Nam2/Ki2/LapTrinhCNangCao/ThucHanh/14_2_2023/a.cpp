#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main(int argc, char* agrv[]) {
    ifstream inFile;
    inFile.open("/PHENIKAA/Ki4/LapTrinhCNangCao/14_2_2023/data.txt");
    if (!inFile.is_open()) {  // inFile.fail()
        cout << "unable to open file!\n";
        exit(0);
    }
    string line;
    int sum = 0;
    while (getline(inFile, line)) {
        istringstream iss(line);
        string token, ss;
        int num;
        while (getline(iss, token, ',')) {
        }
        num = stoi(token);
        sum += num;
    }
    inFile.close();
    ofstream outFile;
    outFile.open("/PHENIKAA/Ki4/LapTrinhCNangCao/14_2_2023/result.txt");
    outFile << "Sum = " << sum << endl;
    outFile.close();
}