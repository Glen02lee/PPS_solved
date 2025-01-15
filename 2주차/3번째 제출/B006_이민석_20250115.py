from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    
    for neighbor in sorted(graph[v]):  # 작은 번호부터 방문
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def bfs(graph, v, n):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for neighbor in sorted(graph[node]):  # 작은 번호부터 방문
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

n, m, x = map(int, input().split())  # 정점, 간선, 시작점
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

visited = [False] * (n + 1)
dfs(graph, visited, x)
print()
bfs(graph, x, n)
"""
DFS와 BFS를 두개 다사용하여 리스트를 탐색한 결과를 출력하는 문제이다.
C로 구현을 해봤어서 구현한 코드를 파이썬으로 바꿔보며 코드를 작성했다.
문제에서 요구하는 출력순서를 맞추게 위해 sorted()를 사용하여 작은번호부터 방문하였다
탐색 방법의 차이에 따라서 그래프의 출력순서가 달라진다는 것을 다시한번 복기하는 코드가 되었다.
"""
