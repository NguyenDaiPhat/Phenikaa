#include <iostream>
#include <vector>
#include <algorithm>
#include<set>
using namespace std;
template <typename T> 
int countOccurrences(const vector<T> &vec, const T &x)
{
    int count = 0;
    for (const auto &element : vec)
    {
        if (element == x)
        {
            count++;
        }
    }
    return count;
}

template <typename T>
void removeValue(vector<T> &vec, const T &x)
{
    vec.erase(remove(vec.begin(), vec.end(), x), vec.end());
}

template <typename T>
vector<int> findIndices(const vector<T> &vec, const T &x)
{
    vector<int> indices;
    for (int i = 0; i < vec.size(); i++)
    {
        if (vec[i] == x)
        {
            indices.push_back(i);
        }
    }
    return indices;
}

template <typename Container>
void printContainer(Container C)
{
    for (auto element : C)
    {
        cout << element << " ";
    }
    cout << endl;
}

int main()
{
    vector<int> vec{1, 2, 3, 4, 1, 5, 6, 1, 7};
    cout << "Vector ban đầu: ";
    for (const auto &element : vec)
    {
        cout << element << " ";
    }
    cout << endl;
    int count = countOccurrences(vec, 1);
    cout << "Số lần xuất hiện của giá trị 1: " << count << endl;
    removeValue(vec, 1);
    cout << "Vector sau khi xóa giá trị 1: ";
    for (const auto &element : vec)
    {
        cout << element << " ";
    }
    cout << endl;
    vector<int> indices = findIndices(vec, 2);
    if (indices.empty())
    {
        cout << "Không tìm thấy giá trị 2 trong vector." << endl;
    }
    else
    {
        cout << "Vị trí của giá trị 2 trong vector: ";
        for (const auto &index : indices)
        {
            cout << index << " ";
        }
        cout << endl;
    }

    vector<int> vec1{1, 2, 3, 4, 5};
    printContainer(vec1);

    set<string> mySet1{"cpple", "banana", "cherry"};
    printContainer(mySet1);

    return 0;
}
