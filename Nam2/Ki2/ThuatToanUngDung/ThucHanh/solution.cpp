#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
struct Input {
    vector<float> t;
    int numJobs;
    int numMachines;
    Input() {}
};
struct Solution {
    Input* data;
    vector<unordered_set<int>> schedule;
    vector<float> sumT;
    Solution(Input* data) {
        this->data = data;
        for (int i = 0; i` < data->numMachines; ++i)
    }
}
void insertJob(int jobID, int machineID){
    schedule[machineID].insert(jobID);
    sumT[machineID] +=data->
}
void  