#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    string name;
    int age;
    for (int i = 1; i < argc; ++i) {
        if (string(argv[i]) == string("-n")) {
            name = argv[i + 1];
        } else if (string(argv[i]) == string("-a")) {
            age = stoi(argv[i + 1]);
        }
    }
    cout << "hello " << name << " " << 10 + age << " tuoi" << endl;
    return 0;
}
