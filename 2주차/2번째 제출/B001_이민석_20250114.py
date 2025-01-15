#PPS "B001"
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    
    return len(visited) - 1  # 1번 제외

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 쌍의 수

graph = {i: set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print(bfs(graph, 1))

"""
문제에서 나와있는 것처럼, 그래프를 이용한다는 점에서 BFS나 DFS를 사용해야할 것 같다는 생각이 들었다
A 문제를 풀면서 익혔던 set은 중복을 자동적으로 방지해주고 빠른 탐색 속도를 유지할 수 있다
나는 개인적으로 바이러스가 퍼진다고 할때, 한점을 중심으로 물결처럼 퍼진다고 상상이 된다
그래서 직관적으로 bfs를 사용해야한다고 생각했고, 예시에서처럼 불필요하게 탐색을 해야하는 경우를 대비하기 위해서
dfs보다는 bfs를 사용했다.
"""