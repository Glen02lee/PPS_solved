#PPS "B020"
def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, number + matrix[ddx][ddy])

matrix = [list(input().split()) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
print(len(result))

'''
처음에는 BFS를 구현하여 구현해보니 계속해서 런타임 오류가 났다
큐의 크기가 계속해서 커진다는 점을 염두에 두고 DFS로 다시 구현하였다
'''