#include<iostream>
#include<vector>
using namespace std;
template<typename T>
void in(T x){
    cout<<x<<endl;
}

template <typename T>
T in(T x, T y){
    if(x>y)return x;
    else return y;
}


int main(int argc, char* argv[]){
    int a = 12,b = 11;
    cout<<in(a,b);
    return 0;
}
