#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> ascending = {1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> descending = {8, 7, 6, 5, 4, 3, 2, 1};
    
    vector<int> mixed(8);
    for (int i = 0; i < 8; i++)
        cin >> mixed[i];
    
    if (mixed == ascending) {
        cout << "ascending";
    } else if (mixed == descending) {
        cout << "descending";
    } else {
        cout << "mixed";
    }
    
    return 0;
}
/*
오름차순, 내림차순 배열을 만들고 그냥 비교하게 만들었다.
*/