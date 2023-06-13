#include <iostream>
#include <vector>
using namespace std;
class SV
{
public:
    int id;
    string name;
    const string sex;
    int age;
    float gpa;

    SV() {}
    SV(int id, string name, string sex, int age, float gpa) : id(id), name(name), sex(sex), age(age), gpa(gpa)
    {
    }
    virtual void disPlay() = 0;
    // {
    //     cout << "Animal " << id << " " << name << endl;
    // }
};
class SV_CNTT : public SV
{
public:
    float color;
    SV_CNTT() {}
    SV_CNTT(int id, string name, string ) : Animal(id, name), color(color) {}
    void disPlay() override
    {
        cout << "Dog " << id << " " << name << " " << color << endl;
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
};

void disPlay(Animal &a)
{
    a.disPlay();
}

int main()
{
    // Animal a(1, "ani");
    Dog d(2, "Do", "black");
    Goose g(3, "Goo", 4);
    disPlay(d);
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