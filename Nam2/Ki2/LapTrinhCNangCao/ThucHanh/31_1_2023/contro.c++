#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int &b = a;
    b++;
    cout << a << " " << b << endl;

    int pi = 10;
    int *i = &pi;
    (*i)++;
    int *j = &(*i);
    cout << *j;
    return 0;
}