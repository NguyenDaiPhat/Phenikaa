#include<iostream>
#include<sstream>
#include<string>
using namespace std;
bool IsNumberic(char c){
    if(c >= '0' && c <='9')  return true;
    return false;
}
// 4 den 12
// 1.1111111
// 11.111111
// 111.11111
// 012345678
// i = 1 => đánh dấu đằng trước là 0
// 01234567
bool check(string s){
    if(s.length() >= 13 || s.length() <= 3) return false;
    for(int i = 1; i< i+2; i++){
        
        for(int j = i+1; j<s.length(); j++){
            for(int k = j+1; k<s.length(); k++){

            }
        }
    }
}
int main(){
    string s;

    return 0;
}