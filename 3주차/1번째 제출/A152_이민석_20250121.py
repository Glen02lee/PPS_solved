#PPS "A152"
def max_stair_score(n, score):
    if n == 1:
        return score[0]
    if n == 2:
        return score[0] + score[1]
    
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    # DP
    for i in range(3, n):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

    return dp[-1]

n = int(input())
score = [int(input()) for _ in range(n)]

# 결과 출력
print(max_stair_score(n, score))

'''
이번 코드도 함수를 사용하여 작성하였다.
처음에는 그저 막무가내로 여러 반복문을 통해 점수를 계산하였는데 재귀형태로 
함수를 불러와서 사용하면 된다고 생각했다


'''