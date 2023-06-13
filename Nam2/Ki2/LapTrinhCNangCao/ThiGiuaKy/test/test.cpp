#include<sstream>
#include<iostream>
#include<string>
using namespace std;
int main (){
    string s = "hiih";
    istringstream iss(s);
    string token;
    getline(iss,token, ';');
    cout<<token;
    return 0;
}