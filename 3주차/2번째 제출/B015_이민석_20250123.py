#PPS "B015"
from collections import deque

def count_reachable_stones(n, A, s):
    visited = [False] * n  # 방문 여부 기록
    queue = deque([s - 1])
    visited[s - 1] = True

    reachable_count = 1

    while queue:
        current = queue.popleft()

        left = current - A[current]
        if 0 <= left < n and not visited[left]: 
            visited[left] = True
            queue.append(left)
            reachable_count += 1

        right = current + A[current]
        if 0 <= right < n and not visited[right]:
            visited[right] = True
            queue.append(right)
            reachable_count += 1

    return reachable_count

n = int(input())
A = list(map(int, input().split())) 
s = int(input())
print(count_reachable_stones(n, A, s))

'''
A는 현재 돌에서 왼쪽이나 오른쪽으로 점프 할 수 있는 거리가 된다
이 부분에서 너비 우선 탐색으로 구현해야겠다고 생각했다
큐를 이용하면 먼저 방문한 돌을 먼저 처리할 수 있기 때문에
탐색의 순서를 유지하면서 최단 경로로 탐새할 수 있다
'''
