#include "Food.cpp"

#include <vector>
class NonCFood : public Food
{
private:
    double weight;

public:
    NonCFood() {}
    NonCFood(string name, double price, double weight) : Food(name, price)
    {
        this->weight = weight;
    }
    void display()
    {
        cout << "Name: " << Food::getName() << endl;
        cout << "Price: " << Food::getPrice() << endl;
        cout << "Weight: " << this->weight << endl;
    }
    double getWeight()
    {
        return weight;
    }
    static void sortWeight(vector<NonCFood> &vt)
    {
        for (int i = 0; i < vt.size() - 1; i++)
        {
            for (int j = i + 1; j < vt.size(); j++)
            {
                if (vt[j].weight < vt[i].weight)
                {
                    swap(vt[j], vt[i]);
                }
            }
        }
    }
};
