#PPS "A211"
n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    dp[i] = a[i]
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j] + a[i]:
            dp[i] = dp[j] + a[i]

print(max(dp))

'''
동적 계획법을 통해 테이블을 채워가며
가장 긴 증가하는 부분 수열의 합을 구하면 된다

'''