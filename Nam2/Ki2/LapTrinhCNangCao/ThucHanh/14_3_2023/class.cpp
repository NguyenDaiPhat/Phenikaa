#include <iostream>
#include <string>
using namespace std;
class Golem {
   public:
    Golem() {
        hp = 100;
        damage = 100;
    }
    Golem(int hp, int damage) {
        this->hp = hp;
        this->damage = damage;
    }
    int hp;
    void laugh() {
        cout << "hehehe" << endl;
    }
    int getDam() {
        return damage;
    }

   private:
    int damage;
};
class Snake {
   public:
    int hp;
    int damage;
    float poison;
    string name;
    float weight, height;
    void attack() {
        cout << "can nhau di" << endl;
    }
    void talk() {
        cout << "loi thi tham cua ran" << endl;
    }
    Snake(int hp, int damage, float poison, string name, float weight, float height) : hp(hp), damage(damage), poison(poison), name(name), weight(weight), height(height) {
        // cout << "A snake has been created\n";
    }
    void showInfo() {
        cout << hp << " " << damage << " " << poison << " " << name;
    }
    float bmi() {
        return weight / (height * 2);
    }
};

class Dog {
   private:
    string ownerName;

   public:
    string name;
    int age;
    const char sex = 'f';
    float height;
    float weight;
    string breed;
    void setOwner(string ownerName) {
        this->ownerName = ownerName;
    }
    void sua() {
        cout << "gau gau gau\n";
    }
    void displayInfo() {
        cout << "hello " << name << " tuoi " << age << " sex " << sex << " height " << height << " weight " << weight << " breed " << breed << " Owner Name " << ownerName << endl;
    }
    void TangTuoi() {
        age++;
    }
    Dog() {}
    Dog(string name, int age, float height, float weight, string breed) : name(name), age(age), height(height), weight(weight), breed(breed) {
        cout << "Mot con cho vua ra doi\n";
    }
    string getOwnerName() { return ownerName; }
    friend void display(const Dog& d);
};

void display(const Dog& d) {
    cout << d.ownerName << endl;
}

int main() {
    Golem golem(10, 10);
    // cout << golem.hp << " " << golem.getDam();
    Snake snake(100, 10, 1.1, "cc", 20, 1.5);
    // cout<<snake.bmi()<<" ";
    // snake.showInfo();
    Dog dog("meo", 1, 50, 5, "alaska");
    dog.setOwner("phat");
    dog.displayInfo();
    display(dog);
}