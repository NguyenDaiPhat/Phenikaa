#include <iostream>
using namespace std;
class Animal {
   private:
    /* data */
   public:
    string Name;
    int Age;
    const char Sex;
    float weight;
    Animal() : Sex('-') {}
    Animal(string Name, int Age, char Sex, float weight) : Name(Name), Age(Age), Sex(Sex), weight(weight) {
        cout << "A animal has been created";
    }
    void showInfo() {
        cout << Name << " " << Age << " " << Sex << " " << weight;
    }
};

class Dog : public Animal {
   public:
    string ownerName;
    Dog(string Name, int Age, char Sex, float weight, string ownerName) : Animal(Name, Age, Sex, weight), ownerName(ownerName) {
        cout << "a dog has been created";
    }
    void showInfo() {
        cout << Name << " " << Age << " " << Sex << " " << weight << " " << ownerName;
    }
};

int main() {
    Animal a;
    Dog d("meo", 10, 'F', 10.1, "saka");
    d.showInfo();
    return 0;
}