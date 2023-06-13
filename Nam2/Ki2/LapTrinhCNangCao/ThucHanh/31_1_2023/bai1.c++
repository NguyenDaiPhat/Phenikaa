#include <iostream>
using namespace std;

int main() {
    double numble = 3.14;
    int num1 = int(numble);
    int num2 = (int)numble;
    int num3 = static_cast<int>(numble);
    int num4 = numble;
    cout << num1 << " " << num2 << " " << num3 << " " << num4;
    return 0;
}