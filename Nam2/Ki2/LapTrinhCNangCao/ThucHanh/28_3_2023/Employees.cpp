#include <iostream>
using namespace std;
class Employee {
   public:
    string ID;
    string Name;
    int Age;
    const char Sex;
    string Address;
    Employee() : Sex('-') {}
    Employee(string ID, string Name, int Age, char Sex, string Address) : ID(ID), Name(Name), Age(Age), Sex(Sex), Address(Address) {
        cout << "A employee has been created";
    }
};

class Fulltime_Employee : public Employee {
   public:
    float Salary;
    Fulltime_Employee(string ID, string Name, int Age, char Sex, string Address, float Salary)
        : Employee(ID, Name, Age, Sex, Address), Salary(Salary) {
        cout << "a fulltime_employee has been created" << endl;
    }
    void inInfo() {
        cout << ID << " " << Name << " " << Age << " " << Sex << " " << Address << " " << Salary;
    }
};


int main() {
    return 0;
}