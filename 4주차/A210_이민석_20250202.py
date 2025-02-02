#PPS "A210"
import sys

def sticker(n, a, b):
    dp = [[0 for _ in range(2)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + a[i - 1])
        dp[i][1] = max(dp[i - 1][0] + b[i - 1], dp[i - 1][1])
    return max(dp[n][0], dp[n][1])

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    print(sticker(n, a, b))
    
'''
이 코드는 일종의 동적 계획법이라고도 볼 수 있을 것 같다
두 가지 스티커 배열에서 선택 가능한 최적의 방법을 찾아 최대로 얻을 수 있는 점수를 게산하고
dp배열을 통해 점수를 계산하며 이전 열에서 가능한 선택을 고려하여 최적의 결과를 도출해내는 것이기 때문이다
'''