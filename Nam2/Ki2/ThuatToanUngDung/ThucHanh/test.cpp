#include <iostream>
#include <vector>
using namespace std;
bool checkTuongThich(vector<int>& bag, int itemID, vector<Item>& danhsachItem, vector<vector<int>>& traTuongThich) {
    for (auto idvaTrongTui : bag) {
        int type1 = danhsachItem[itemID].type;
        int type2 = danhsachItem[idvaTrongTui].type;
        if (traTuongThich[type1][type2] == 0) return false;
    }
    return true;
}
bool checkSucKhang(vector<int>& bag, float carryValue, int itemID, vector ){
    bool ok_SucKhang = checkSucKhang(bags[bag], carry[bag], item, items);
    if(ok_DungLuong && ok_TuonngThich && ok_SucKhang){
        chosenBag = bag;
        break;
    }
}
int main(int argc, char *argv[]) {
    string path = "";
    vector<vector<int>> bags;
    vector<float> carry;
}
