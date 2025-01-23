#PPS "B019"
from collections import deque

# BFS 탐색
def BFS(x, y, grid, visited):
    q = deque([(x, y)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 (4방향)
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))

def count_regions(grid, n, is_colorblind):
    visited = [[False] * n for _ in range(n)]
    region_count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                color = grid[i][j]
                if is_colorblind and color == 'G':  # G  --> R
                    color = 'R'
                BFS(i, j, grid, visited)
                region_count += 1
                
    return region_count

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

normal_region_count = count_regions(grid, n, False)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

colorblind_region_count = count_regions(grid, n, True)

print(normal_region_count)
print(colorblind_region_count)

'''
BFS를 통해 구현하였다.
BFS(x, y, grid, visited) 함수는 시작 좌표 (x, y)에서부터 BFS를 통해
연결된 같은 색의 칸들을 모두 방문한다
나는 정상적인 색각, 색약의 경우를 나누어 각각 탐색한 후 지역의 개수를 구하고자 했다
따라서 BFS를 사용항 각 칸을 방문하고 연결된 같은 색의 칸들을 하나의 지역으로 게산했다
visited 배열을 활용하여 중복을 방지했다.
'''