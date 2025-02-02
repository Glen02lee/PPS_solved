#PPS "A200"
N = int(input())
dp = [False] * (N + 1)

dp[0] = False
if N >= 1:
    dp[1] = True 
if N >= 2:
    dp[2] = False 
if N >= 3:
    dp[3] = True 

for i in range(4, N + 1):
    if not dp[i - 1] or not dp[i - 3]:
        dp[i] = True

if dp[N]:
    print("CY")
else:
    print("SK")
'''
이 문제는 돌을 3개까지 가져갈 수 있는 조건을 걸어 예외사항을 처리해줘야했다
4부터는 동적 계획법을 통해 구현할 수 있지만 이전까지는 경우의 수에 맞게
예외처리를 해줘야했다
돌이 0일 때는 상근이가 질 수 밖에 없음
0개의 돌에서는 상근이가 이길 수 없음
1개의 돌은 상근이가 가져가면 이김
2개의 돌에서는 상근이가 가져가면 창영이가 이김
3개의 돌에서는 상근이가 3개를 가져가면 이김
4부터 N까지 동적 계획법으로 계산
'''