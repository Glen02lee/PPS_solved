class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

/*
배열을 받아서 +1을 하는 문제
생각해야할것은 9에 1을 더해 carry가 발생하는 경우만 고려해주면 될 것 같았다.
일반적인 경우는 그냥 +1을 해주면 되고,
9인 경우 만약 다음 숫자도 9라면 계속해서 0으로 바꿔주는 작업을 해주면 된다.
만약 9999인 경우도 있을 수 있기때문에 배열 처음에 1을 넣어준다
*/