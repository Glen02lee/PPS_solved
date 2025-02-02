#PPS "A222"
def binomial_coefficient(n, k):
    # 파스칼의 삼각형 방식
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(min(i, k) + 1): 
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    return dp[n][k]

n, k = map(int, input().split())
print(binomial_coefficient(n, k))
