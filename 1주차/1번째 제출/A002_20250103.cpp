class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;

        for (int i = 0; i < numRows; i++) {
            vector<int> row(i + 1, 1);
            for (int j = 1; j < i; j++) {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
            triangle.push_back(row);
        }

        return triangle;
    }
};

/*
이 문제는 파스칼의 삼각형을 구현하는 문제다
2차원 동적 배열을 위한 벡터를 구현하였다.
파라미터는 몇번째 층을 의미한다.
파스칼의 삼각형은 배열의 양 끝값은 무조건 1로 고정이 된다
[1] [1 2 1]처럼 말이다.
따라서 양끝값을 제외한 부분에 윗층의 저장된 숫자들을 더해주는 방식으로 구현하였다.
/