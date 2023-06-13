#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Define a struct to represent an item
struct Item
{
    int size;
    int capacity;
    vector<int> compatible_items; // indices of compatible items
};

// Define a struct to represent a bin
struct Bin
{
    int capacity;
    vector<int> items; // indices of items in the bin
};

void bubbleSort(vector<Item> &items)
{
    int n = items.size();
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (items[j].capacity < items[j + 1].capacity)
            {
                swap(items[j], items[j + 1]);
            }
        }
    }
}
// Function to perform first fit decreasing heuristic
vector<Bin> firstFitDecreasing(vector<Item> &items, int bin_capacity)
{
    // Sort the items in non-increasing order of capacity
    bubbleSort(items);

    // Create an empty bin to start with
    vector<Bin> bins;
    bins.push_back(Bin{bin_capacity, vector<int>()});

    // Iterate over the items and place each item in the first bin that can accommodate it
    for (auto &item : items)
    {
        // Find the first bin that can accommodate the item
        bool bin_found = false;
        for (auto &bin : bins)
        {
            // Check if the bin can accommodate the item and the item is compatible with all items in the bin
            bool can_fit = item.size <= bin.capacity;
            bool is_compatible = all_of(bin.items.begin(), bin.items.end(), [&](int i)
                                        { return find(item.compatible_items.begin(), item.compatible_items.end(), i) != item.compatible_items.end(); });
            if (can_fit && is_compatible)
            {
                // Add the item to the bin
                bin.items.push_back(&item - &items[0]);
                bin.capacity -= item.size;
                bin_found = true;
                break;
            }
        }
        // If no bin can accommodate the item, create a new bin
        if (!bin_found)
        {
            bins.push_back(Bin{bin_capacity - item.size, vector<int>{&item - &items[0]}});
        }
    }
    return bins;
}

// Function to print the contents of each bin
void printBins(vector<Bin> &bins, vector<Item> &items)
{
    for (int i = 0; i < bins.size(); i++)
    {
        cout << "Bin " << i + 1 << ": [";
        for (int j = 0; j < bins[i].items.size(); j++)
        {
            int idx = bins[i].items[j];
            cout << "item" << idx + 1 << " ";
        }
        cout << "]" << endl;
    }
}

int main()
{
    // Define the input data
    vector<Item> items = {
        {10, 20, {1, 2, 3}},
        {5, 10, {0}},
        {7, 15, {0, 3}},
        {3, 5, {2}}};
    int bin_capacity = 25;

    // Run the first fit decreasing heuristic
    vector<Bin> bins = firstFitDecreasing(items, bin_capacity);

    // Print the contents of each bin
    printBins(bins, items);

    return 0;
}