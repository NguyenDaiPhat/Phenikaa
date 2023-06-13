#pragma once
// #include "Food.cpp"
#include "NonCFood.cpp"
#include "CannedFood.cpp"
int main()
{
    vector<CannedFood> cfoods(3);
    cfoods[0] = CannedFood("A", 3.0, 3);
    cfoods[1] = CannedFood("B", 2.0, 2);
    cfoods[2] = CannedFood("C", 1.0, 1);

    int maxNumberBoxIndex = 0;
    for (int i = 0; i < cfoods.size(); i++)
        if (cfoods[i].getNumberBox() > cfoods[maxNumberBoxIndex].getNumberBox())
            maxNumberBoxIndex = i;

    cfoods[maxNumberBoxIndex].setPrice(cfoods[maxNumberBoxIndex].getPrice());

    CannedFood::sortNumberBox(cfoods);
    for (auto v : cfoods)
        v.display();

    vector<NonCFood> ncfoods(3);
    ncfoods[0] = NonCFood("A", 1.0, 1);
    ncfoods[1] = NonCFood("B", 2.0, 1);
    ncfoods[2] = NonCFood("C", 3.0, 1);

    int maxWeightIndex = 0;
    for (int i = 0; i < ncfoods.size(); i++)
        if (ncfoods[i].getWeight() > ncfoods[maxWeightIndex].getWeight())
            maxWeightIndex = i;

    ncfoods[maxWeightIndex].setPrice(ncfoods[maxWeightIndex].getPrice());

    NonCFood::sortWeight(ncfoods);
    for (auto v : ncfoods)
        v.display();
}
