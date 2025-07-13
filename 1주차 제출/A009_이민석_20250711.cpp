#include <string>
#include <cstring>
#include <vector>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if (s.length() != 4 && s.length() != 6) answer = false;

    for (char& c : s) {
        if (!isdigit(c)) answer = false;
    }
    return answer;
}

/*
문장의 길이가 4,6이어야만하고 숫자로만 이루어져야한다는 조건을 넣었다.
*/