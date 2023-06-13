#include <fstream>
#include <math.h>
#include <iostream>
#include <vector>
using namespace std;

struct Game {
    int Rank;
    string Name;
    string Platform;
    int Year;
    string Genre;
    string Publisher;
    double NA_Sales;
    double EU_Sales;
    double JP_Sales;
    double Other_Sales;
    double Global_Sales;
};
int main(int argc, char* argv[]) {
    string path, PublisherName, gameGenre;
    for (int i = 1; i < argc; ++i) {
        if (string(argv[i]) == string("-f")) {
            path = argv[i + 1];
        } else if (string(argv[i]) == string("-p")) {
            PublisherName = stoi(argv[i + 1]);
        } else if (string(argv[i]) == string("-g")) {
            PublisherName = stoi(argv[i + 1]);
        }
    }
    ifstream inFile;
    inFile.open(path);
    if (!inFile.is_open()) {  
        cout << "unable to open file!\n";
        exit(0);
    }
    vector<Game> game;
    string s1;
    getline(inFile, s1);
    while(getline(inFile, s1)){
        Game gameC;
        getline(inFile, s1, ',');gameC.Rank = stoi(s1);
        getline(inFile, s1, ',');gameC.Name = s1;
        getline(inFile, s1, ',');gameC.Platform = s1;
        getline(inFile, s1, ',');gameC.Year = stoi(s1);
        getline(inFile, s1, ',');gameC.Genre = s1;
        getline(inFile, s1, ',');gameC.Publisher = s1;
        getline(inFile, s1, ',');gameC.NA_Sales =stod(s1);
        getline(inFile, s1, ',');gameC.EU_Sales = stod(s1);
        getline(inFile, s1, ',');gameC.JP_Sales = stod(s1);
        getline(inFile, s1, ',');gameC.Other_Sales = stod(s1);
        getline(inFile, s1, ',');gameC.Global_Sales = stod(s1);
        game.push_back(gameC);
    }
    double sum = 0;
    int dem = 0;
    for (int i = 0; i < game.size(); i++){
        if(game[i].Publisher == PublisherName){
            sum += game[i].Global_Sales;
            cout << "Cac game duoc phat hanh thoa man la: " << game[i].Name;
        }
        if (game[i].Genre == gameGenre) {
            dem++;
        }
    }
    cout << endl;
    cout << "Tong doanh thu cua cac game la: "<< sum<<endl;
    cout << "Tong so luong game trong data thuoc the loai gamegenre la: " << dem;
    inFile.close();
    ofstream outFile;
    outFile.open("C:/Users/OS/Desktop/output.txt");
    if (!inFile.is_open()) {
        cout << "unable to open file!\n";
        exit(0);
    }
    for (int i = 0; i < game.size()-1; i++) {
        for (int j = i + 1; j < game.size();j++){
            if(game[i].Global_Sales < game[j].Global_Sales){
                Game tg = game[i];
                game[i] = game[j];
                game[j] = tg;
            }
        }
    }
    outFile << "Top 10 game co doanh thu cao nhat "<< endl;
    for (int i = 0; i < 9;i++){
        outFile << game[i].Name << endl;
    }
    outFile.close();
    return 0;
}
