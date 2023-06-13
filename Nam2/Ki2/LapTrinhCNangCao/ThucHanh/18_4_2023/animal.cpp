#include <iostream>
#include <vector>
#include<sstream>
using namespace std;
class Animal
{
public:
    int id;
    string name;
    Animal() {}
    Animal(int id, string name) : id(id), name(name)
    {
    }
    virtual void disPlay() = 0;
    // {
    //     cout << "Animal " << id << " " << name << endl;
    // }
    // vitrual ostream& operator <<(ostream& os, const Animal& a)=0;
    virtual string getString() =0;
};

class Dog : public Animal
{
public:
    string color;
    Dog() {}
    Dog(int id, string name, string color) : Animal(id, name), color(color) {}
    void disPlay() override
    {
        cout << "Dog " << id << " " << name << " " << color << endl;
    }
    string getString() override{
        stringstream s;
        s<< "DOG: " <<id<< " "<< name<<" "<< color<<"\n";
        return s.str();
    }
};

class Goose : public Animal
{
public:
    float weight;
    Goose() {}
    Goose(int id, string name, float weight) : Animal(id, name), weight(weight) {}
    void disPlay() override
    {
        cout << "Goose" << id << " " << name << " " << weight << endl;
    }
    string getString() override
    {
        stringstream s;
        s << "Goose: " << id << " " << name << " " << weight << "\n";
        return s.str();
    }
};

ostream& operator <<(ostream& os, Animal &a){
    os << a.getString();
    return os;
}

void disPlay(Animal &a)
{
    a.disPlay();
}

int main()
{
    // Animal a(1, "ani");
    Dog d(2, "Do", "black");
    Goose g(3, "Goo", 4);
    // disPlay(d);
    cout<<g;
    // a.disPlay();
    // d.disPlay();
    // g.disPlay();
    // vector<Animal*> v;
    // v.push_back(&a);
    // v.push_back(&d);
    // v.push_back(&g);
    // v[0]->disPlay();
    // v[1]->disPlay();
    // v[2]->disPlay();

    // vector<Animal > v1;
    // v1.push_back(a);
    // v1.push_back(d);
    // v1.push_back(g);
    // v1[0].disPlay();
    // v1[1].disPlay();
    // v1[2].disPlay();

    return 0;
}