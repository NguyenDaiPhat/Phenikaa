#include <iostream>
#include <vector>
using namespace std;
class Student {
   public:
    int ID;
    string name;
    int age;
    const char sex;
    string lop;
    float gpa;
    Student(char sex) : sex(sex) {
        cout << "A student created with sex" << endl;
    }
    Student(int ID, string name, int age, char sex, string lop, float gpa)
        : ID(ID), name(name), age(age), sex(sex), lop(lop), gpa(gpa) {
        cout << "A Student created" << endl;
    }
    // copy constructor
    Student(const Student& s) : sex(s.sex) {
        ID = s.ID;
        name = s.name;
        age = s.age;
        lop = s.lop;
        gpa = s.gpa;
        cout << "A COPY of student " << ID << "has been created" << endl;
    }
    // assignment operator
    Student& operator=(const Student& s) {
        gpa = s.gpa;
        cout << "A assignment operator has been created " << endl;
        return *this;
    }
};
int main() {
    // Student a(1, "a", 10, 'f', "1A", 4);
    // Student b('f');
    // b.gpa = 10;
    // Student c(a);
    // Student d = a;  //
    // cout << "Before " << c.gpa << endl;
    // c = b;
    // cout << "After " << c.gpa << endl;
    vector<Student> v;
    for (int i = 0; i < 2; i++) {
        Student s('f');
        s.ID = i;
        v.push_back(s);
    }
    return 0;
}