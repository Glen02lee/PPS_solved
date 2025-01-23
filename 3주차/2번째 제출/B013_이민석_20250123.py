#PPS "B013"
from collections import deque

def solve(A, B, C):
    # 경우의 수를 담을 큐
    q = deque()
    q.append((0, 0))  # (a, b) 상태로 시작

    # 방문 여부 저장
    visited = [[False] * (B + 1) for _ in range(A + 1)]
    visited[0][0] = True

    answer = []

    def pour(x, y):
        if not visited[x][y]:
            visited[x][y] = True
            q.append((x, y))
            
    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)

        # A에서 B
        water = min(x, B - y)
        pour(x - water, y + water)

        # A에서 C
        water = min(x, C - z)
        pour(x - water, y)

        # B에서 C
        water = min(y, C - z)
        pour(x, y - water)

        # B에서 A
        water = min(y, A - x)
        pour(x + water, y - water)

        # C에서 A
        water = min(z, A - x)
        pour(x + water, y)

        # C에서 
        water = min(z, B - y)
        pour(x, y + water)
    answer.sort()
    for i in answer:
        print(i, end=" ")

a, b, c = map(int, input().split()) 
solve(a, b, c)
'''
조금 간결하지 못하지만 계속해서 오류가 나서 직관적으로 코딩을 해보니 통과가 되었다
# 가능한 물 옮기기 (from -> to)
        for from_tank, to_tank, to_limit in [
            (a, b, B), (a, c, C),
            (b, a, A), (b, c, C),
            (c, a, A), (c, b, B),
        ]:
처음에는 이런식으로 구현을 한 후 옮길수 있는 물의 양, 새로운 상태를 계산하는 식으로
조금 더 복잡하게 구현했더니 계속 틀렸었다
주석을 이용해 이동경로를 다시 구현하며 코딩을 해보니 문제가 해결되었다

'''