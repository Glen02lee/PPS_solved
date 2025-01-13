#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string s) {
    int len = s.length();
    int min_length = len;

    for (int step = 1; step <= len / 2; step++) {
        string compressed = "";
        string prev = s.substr(0, step);
        int count = 1;

        for (int j = step; j < len; j += step) {
            string current = s.substr(j, step);
            if (prev == current) {
                count++;
            } else {
                if (count > 1) compressed += to_string(count);
                compressed += prev;
                prev = current;
                count = 1;
            }
        }

        if (count > 1) compressed += to_string(count);
        compressed += prev;

        min_length = min(min_length, (int)compressed.length());
    }

    return min_length;
}

/*
문자열을 압축해야하는데, 2글자씩, 3글자씩 압축이 가능하고, 가능한 작은 문장으로 만들어야한다.
브루트포스 알고리즘이 떠올랐다.
어떤 압축이라도 전체의 절반을 넘어가진 못할것이므로, 가능한 모든 압축 단위를 시도하기 위해 절반까지 돌게하였다.
이렇게 찾은 조합으로 문장을 다시돌며 가능한 모든 경우를 판단하고 있다.
*/