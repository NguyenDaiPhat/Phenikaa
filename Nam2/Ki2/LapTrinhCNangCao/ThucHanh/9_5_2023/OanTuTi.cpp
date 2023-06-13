#include<iostream>
using namespace std;
bool check(string &s){

    if(s.length() != 3) return false;
    for(int i = 0; i<s.length(); i++){
        if(s[i]!= 'B' && s[i] != 'G' && s[i] != 'K') return false;
    }
    return true;
}
void getWinner(string s1, string s2){
    int diem=0;
    for(int i = 0; i <s1.length(); i++){
        if(check(s1) && check(s2)){
            if((s1[i] == 'B' && s2[i] == 'G')|| (s1[i] == 'G' && s2[i] == 'K') || (s1[i] == 'K' && s2[i] == 'B')) diem--;
            else if ((s1[i] == 'B' && s2[i] == 'K') || (s1[i] == 'K' && s2[i] == 'G') || (s1[i] == 'G' && s2[i] == 'B')) diem++;
        }
        else cout<<"Sai dinh dang";
    }
    if(diem == 0) cout<< "Hoa";
    else if(diem > 0) cout << "A thang " + diem;
    else cout<< "B thang " + diem*(-1);
}
int main(){
    string s1, s2;
    cin>>s1>>s2;
    getWinner(s1,s2);
    return 0;
}