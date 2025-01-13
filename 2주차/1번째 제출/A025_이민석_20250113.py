#PPS "A025"
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        while n % 4 ==0:
            n //= 4

        return n==1
    
        """
        주어진 수가 4의 거듭제곱인지를 판별하는 함수이다.
        불리언 형식의 함수이므로, 4로 나눈값이 1이면 True, 아니면 False형태로 반환되게 했다.
        """