class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int i = 0, j = 0;

        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) {
                i++;
            }
            j++;
        }
        return i;
    }
};

/*
함수 제작형 문제
최대한 많은 아이들에게 쿠키를 줘야한다는 부분에서 그리디 알고리즘을 떠올림
효율적인 분배를 위해 정렬을 하였다.
이후 아이의 요구에 맞게 쿠키가 있다면 +1을 해주는식으로 구현하였다.
*/