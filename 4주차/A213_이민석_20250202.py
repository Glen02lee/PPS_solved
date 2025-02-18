#PPS "A213"
n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n + 1)
dp[1] = wine[0]
if n >= 2:
    dp[2] = wine[0] + wine[1]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + wine[i - 1], dp[i - 3] + wine[i - 1] + wine[i - 2])

print(dp[n])