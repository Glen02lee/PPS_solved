#PPS "A212"
MOD = 9901

def lion_placement(N):
    dp = [0] * (N + 1)
    dp[0] = 1  
    dp[1] = 3  # 첫 번째 줄에서 (빈칸, 왼쪽 사자, 오른쪽 사자) 총 3가지 경우

    for i in range(2, N + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % MOD  

    return dp[N]

N = int(input())
print(lion_placement(N))
