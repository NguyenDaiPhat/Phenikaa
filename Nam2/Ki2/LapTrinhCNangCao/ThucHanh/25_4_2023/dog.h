#ifndef DOG_H
#define DOG_H
#include<string>
#include <string>
using namespace std;
class Dog{
    public:
    string name;
    int id;
    Dog();
    Dog(int id, string name);

};
#endif // DOG_H

// int main(int argc, char* argv[]){
//     Dog d;
//     return 0;
// }
// g++ multi.cpp dog.cpp -o app
// ./app