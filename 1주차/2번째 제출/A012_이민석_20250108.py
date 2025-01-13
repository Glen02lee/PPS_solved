class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime = [True] * n  
        is_prime[0] = is_prime[1] = False  
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:  
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = False  

        return sum(is_prime)  


    """
    음이 아닌 수중 소수를 카운트하는 문제
    최대한 간단하게 구현하고자 노력했다.
    처음에는 직접 "에라토스테네스의 체"를 구현해볼까 했는데, 
    알고리즘을 살짝 변형하여 더욱 간결하게 구현해보고자 노력했다.
    어차피 n의 제곱근까지 확인하여 소수일경우 그 수의 배수들을 모두 거르는 식으로
    구현을 해보았다.
    """