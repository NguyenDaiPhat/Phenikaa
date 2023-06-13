#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void in(vector<int> v){
    for(int i=0; i<v.size();i++){
        cout << v[i] << "|";
    }  
}
void inSolution(vector<vector<int>> & schedule , vector<float> & sumT){
    float maxT=0;
    for(int m=0; m < schedule.size(); m++){
        cout << " Machine "  << m << " |" << sumT[m] << " |";
        for(int i=0; i<schedule[m].size();i++){
        cout << schedule[m][i] << " ";
        
    }  
    if(maxT < sumT[m]){
        maxT = sumT[m];
    }
    cout << endl;
    }
    cout << "max: "  << maxT <<  endl;
}
void insert(vector<vector<int>> & schedule, vector<float> &t ,vector<int> &sequence, vector<float> &sumT ){
        int numJobs = t.size();
        int numMachines= schedule.size();
    for(auto job : sequence){
        float minTime= 9999;
        int minMachines= -1;
        for(int m=0; m<numMachines;m++){
           if(sumT[m]<minTime){
            minTime=sumT[m];
            minMachines=m;
           }
        }

        // cho job vao minMachines
        schedule[minMachines].push_back(job);
        sumT[minMachines]+= t[job];

        
    }
}
int main(int argc, char* argv[]) {

    vector<float> t= {8,2,9,2,5,7,1,5,7,3};
    int numJobs =t.size();
    int numMachines =4;
    vector<vector<int>>  schedule;
    for (int i=0; i<numMachines; i++){
        schedule.push_back({});
    }
    vector<int> sequence = {0,1,2,3,4,5,6,7,8,9};
    vector<float> sumT(numMachines);

    for(int i=0; i<numJobs; i++){
        for(int j=i+1;j< numJobs ;j++){
            if(t[sequence[j]] > t[sequence[i]]){
                swap(sequence[i],sequence[j]);
            }
        }
    }
    insert(schedule, t, sequence,sumT);
    inSolution(schedule,sumT);
    return 0;
}