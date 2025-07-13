#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    int sn, n;
    cin >> sn;
    vector<vector<int>> score(sn);
    vector<double> over_avg(sn);
    
    for (int i = 0; i < sn; i++) {
        cin >> n;
        score[i].resize(n);
        int sum = 0, count = 0;
        
        for (int j = 0; j < n; j++) {
            cin >> score[i][j];
            sum += score[i][j];
        }
        
        double avg = static_cast<double>(sum) / n;
        for (int j = 0; j < n; j++) {
            if (score[i][j] > avg)
                count++;
        }
        over_avg[i] = static_cast<double>(count) / n * 100;
    }
    
    cout << fixed << setprecision(3);
    for (double percentage : over_avg) {
        cout << percentage << "%\n";
    }
    
    return 0;
}
/*
평균을 분석하면 된다.
소수점을 위한 fixed와 setprecision을 사용하였다.
*/
