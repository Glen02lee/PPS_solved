#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;
    for (int num : arr) {
        if (num % divisor == 0) {
            answer.push_back(num);
        }
    }
    
    if (answer.empty()) {
        answer.push_back(-1);
    } else {
        sort(answer.begin(), answer.end());
    }
    return answer;
}

/*
배열에서 divisor로 나누어 떨어지는 숫자만을 남겨서 반환하기
그냥 새로운 배열을 선언후 거기에 숫자를 넣어 반환하였다
벡터의 개념과 사용방식을 복습하였다.
*/