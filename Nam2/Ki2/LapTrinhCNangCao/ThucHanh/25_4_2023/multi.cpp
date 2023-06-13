#include <iostream>

#include <sstream>
#include <vector>
using namespace std;

class Dog
{
public:
    string name;
    int id;
    Dog();
    Dog(int id, string name);
};
Dog::Dog()
{ // dinh nghia
    cout << "Empty Dog created" << endl;
}
Dog::Dog
{
    cout << "Dog created" << endl;
}
// multi, 