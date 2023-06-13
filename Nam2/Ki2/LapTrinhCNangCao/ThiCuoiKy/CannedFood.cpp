#include "Food.cpp"
#include <vector>

class CannedFood : public Food
{
private:
    int numberBox;

public:
    CannedFood() {}
    CannedFood(string name, double price, int numberBox) : Food(name, price)
    {
        this->numberBox = numberBox;
    }
    int getNumberBox()
    {
        return numberBox;
    }
    void display()
    {
        cout << "Name: " << Food::getName() << endl;
        cout << "Price: " << Food::getPrice() << endl;
        cout << "Number box: " << this->numberBox << endl;
    }
    static void sortNumberBox(vector<CannedFood> &vt)
    {
        for (int i = 0; i < vt.size() - 1; i++)
        {
            for (int j = i + 1; j < vt.size(); j++)
            {
                if (vt[j].numberBox < vt[i].numberBox)
                {
                    swap(vt[j], vt[i]);
                }
            }
        }
    }
};
