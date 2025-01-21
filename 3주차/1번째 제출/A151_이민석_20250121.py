#PPS "A151"
def max_triangle_path(n, triangle):
    dp = [[0] * n for _ in range(n)]
    
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0: #왼쪽
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i: #오른쪽
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:  # 가운데
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    # 최댓값만 반환
    return max(dp[n-1])

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

print(max_triangle_path(n, triangle))
