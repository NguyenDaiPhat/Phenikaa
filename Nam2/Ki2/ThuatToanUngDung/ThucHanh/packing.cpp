#include <algorithm>
#include <iomanip>
#include <iostream>
#include <unordered_set>
#include <vector>
#define CAP 1
using namespace std;
void in(vector<vector<int>>& bags, vector<float>& emmpty_space) {
    for (int i = 0; i < bags.size(); ++i) {
        cout << CAP - emmpty_space[i] << " - ";
    }
}
void next_fit(vector<float>& w, vector<vector<int>>& bags, vector<float>& emmpty_space) {
    bags.push_back({});
    emmpty_space.push_back(CAP);
    for (int itemID = 0; itemID < w.size(); ++itemID) {
        float canNang = w[itemID];
        if (canNang > emmpty_space[emmpty_space.size() - 1]) {
            bags.push_back({});
            emmpty_space.push_back(CAP);
        }
        int last = bags.size() - 1;
        bags[last].push_back(itemID);
        emmpty_space[last] -= canNang;
    }
}

void first_fit(vector<float>& w, vector<vector<int>>& bags, vector<float>& emmpty_space) {
    bags.push_back({});
    emmpty_space.push_back(CAP);
    for (int itemID = 0; itemID < w.size(); ++itemID) {
        float canNang = w[itemID];
        int id_tui_fit = -1;
        for (int tui = 0; tui < bags.size(); ++tui) {
            if (canNang <= emmpty_space[tui]) {
                id_tui_fit = tui;
                break;
            }
        }
        if (id_tui_fit == -1) {
            bags.push_back({});
            emmpty_space.push_back(CAP);
            id_tui_fit = bags.size() - 1;
        }
        bags[id_tui_fit].push_back(itemID);
        emmpty_space[id_tui_fit] -= canNang;
    }
}

void best_fit(vector<float>& w, vector<vector<int>>& bags, vector<float>& emmpty_space) {
    bags.push_back({});
    emmpty_space.push_back(CAP);
    for (int itemID = 0; itemID < w.size(); ++itemID) {
        float canNang = w[itemID];
        int id_tui_fit = -1;
        float min = 9999;
        for (int tui = 0; tui < bags.size(); ++tui) {
            if (canNang <= emmpty_space[tui] && emmpty_space[tui] < min) {
                min = emmpty_space[tui];
                id_tui_fit = tui;
            }
        }
        if (id_tui_fit == -1) {
            bags.push_back({});
            emmpty_space.push_back(CAP);
            id_tui_fit = bags.size() - 1;
        }
        bags[id_tui_fit].push_back(itemID);
        emmpty_space[id_tui_fit] -= canNang;
    }
}

void bfd(vector<float>& w, vector<vector<int>>& bags, vector<float>& emmpty_space) {
    vector<pair<float, int>> items;
    for (int i = 0; i < w.size(); ++i) {
        items.push_back(make_pair(w[i], i));
    }
    sort(items.begin(), items.end(), greater<pair<float, int>>());

    bags.push_back({});
    emmpty_space.push_back(CAP);
    for (auto item : items) {
        float canNang = item.first;
        int id_tui_fit = -1;
        float min = 99999;
        for (int tui = 0; tui < bags.size(); ++tui) {
            if (canNang <= emmpty_space[tui] && emmpty_space[tui] < min) {
                min = emmpty_space[tui];
                id_tui_fit = tui;
            }
        }
        if (id_tui_fit == -1) {
            bags.push_back({});
            emmpty_space.push_back(CAP);
            id_tui_fit = bags.size() - 1;
        }
        bags[id_tui_fit].push_back(item.second);
        emmpty_space[id_tui_fit] -= canNang;
    }
}

int main(int argc, char* argv[]) {
    vector<float> w = {0.5, 0.7, 0.5, 0.2, 0.4, 0.2, 0.5, 0.1, 0.6};
    vector<vector<int>> bags;
    vector<float> empty_space;
    first_fit(w, bags, empty_space);
    in(bags, empty_space);
    return 0;
}
